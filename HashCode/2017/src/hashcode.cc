#include <fstream>
#include <sstream>
#include <vector>

#include "endpoint.hh"
#include "video.hh"


int size_vec(std::vector<int> v)
{
  int sum = 0;
  for (std::size_t i = 0; i < v.size(); i++)
  {
    sum += v[i];
  }
  return sum;
}

std::vector<std::vector<int>> first_fit(std::vector<Video> v, int nb_cache, int size, std::vector<Endpoint> e)
{
  std::vector<std::vector<int>> out;
  for (int i = 0; i < (int)v.size() && i < nb_cache; i++)
  {
    std::vector<int> tmp;
    while (size_vec(tmp) < size)
    {
        bool b = false;
      for (int k = 0; k < (int)e.size(); k++)
      {
        if (e[k].datacenter_latency > 0)
        {
          tmp.push_back(v[i].size);
          b = true;
          break;
        }
      }
        if (b)
          break;
      i++;
    }
    out.push_back(tmp);
  }
  return out;
}
void print(std::vector<std::vector<int>> out, std::string file)
{
  std::ofstream myfile(file + ".out");
  myfile << out.size() << std::endl;
  for (int i = 0; i < (int) out.size(); i++)
  {
    myfile << i;
    for (int j = 0; j < (int) out[i].size(); j++)
    {
      myfile << ' ' << out[i][j];
    }
    myfile << std::endl;
  }
  myfile.close();
}

#include <algorithm>
#include <iostream>


int main(int argc, char** argv)
{
  if (argc != 2)
    return 1;
  std::ifstream in(argv[1]);
  if (!in.is_open())
    return 1;
  std::string line;
  std::getline(in, line);
  std::string video;
  std::istringstream iss_line(line);
  std::getline(iss_line, video, ' ');
  int nb_video = std::stoul(video, nullptr, 10);
  std::vector<Video> videos_vect;
  std::string endpoints;
  std::getline(iss_line, endpoints, ' ');
  int nb_endpoint = std::stoul(endpoints, nullptr, 10);
  std::vector<Endpoint> endpoints_vect;
  std::string requests;
  std::getline(iss_line, requests, ' ');
  int nb_requests = std::stoul(requests, nullptr, 10);
  std::string caches;
  std::getline(iss_line, caches, ' ');
  int nb_caches = std::stoul(caches, nullptr, 10);
  std::string caches_s;
  std::getline(iss_line, caches_s, ' ');
  int caches_size = std::stoul(caches_s, nullptr, 10);
  std::getline(in, line);
  std::istringstream video_line(line);
  std::string current_video;
  for (auto i = 0; i < nb_video; i++)
  {
    std::getline(video_line, current_video, ' ');
    int video_size = std::stoul(current_video, nullptr, 10);
    videos_vect.push_back({video_size, nb_endpoint});
  }
  for (auto i = 0; i < nb_endpoint; i++)
  {
    std::getline(in, line, ' ');
    int dl = std::stoul(line, nullptr, 10);
    endpoints_vect.push_back({dl, nb_caches});
    std::getline(in, line);
    int nb_caches_local = std::stoul(line, nullptr, 10);
    for (auto j = 0; j < nb_caches_local; j++)
    {
      std::getline(in, line, ' ');
      int c = std::stoul(line, nullptr, 10);
      std::getline(in, line);
      int l = std::stoul(line, nullptr, 10);
      endpoints_vect.rbegin()->latency_vect[c] = l;
    }
  }
  for (auto i = 0; i < nb_requests; i++)
  {
    std::getline(in, line, ' ');
    int video_idx = std::stoul(line, nullptr, 10);
    std::getline(in, line, ' ');
    int end = std::stoul(line, nullptr, 10);
    std::getline(in, line);
    int req = std::stoul(line, nullptr, 10);
    videos_vect[video_idx].end[end] += req;
  }

  std::vector<std::vector<int>> v(nb_caches);
  for (std::size_t i = 0; i < v.size(); i++)
  {
    int r = rand() % nb_caches;
    if (std::find(v[i].begin(), v[i].end(), r) != v[i].end())
      i--;
    else
      v[i].push_back(r);
  }
  print(v, std::string(argv[1]));
  return 0;
}
