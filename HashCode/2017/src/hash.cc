#include <fstream>
#include <sstream>
#include <vector>
#include <iostream>
#include <algorithm>

#include "endpoint.hh"
#include "video.hh"


using ress = std::vector<std::vector<int>>;

std::vector<int> boola = std::vector<int>{};
int pos;

std::vector<Video> videos_vect;
std::vector<Endpoint> endpoints_vect;

int max_vector(std::vector<long> vect)
{
  int max = 0;
  for (const auto& it : vect)
  {
    if (it > vect[max])
      max = it;
  }
  return max;
}

int min_vector(std::vector<int> vect)
{
  int min = 0;
  for (const auto& it : vect)
  {
    if (it < vect[min])
      min = it;
  }
  return min;
}

int best_size(std::vector<Video> video, int remain, int cache)
{
  int mini = remain;
  auto a = 0;
  for (; a < (int)video.size(); a++)
  {
    auto max = max_vector(videos_vect[a].end);
    auto min = min_vector(endpoints_vect[max].latency_vect);
    if (video[a].size <= remain && video[a].size < mini && boola[a] == 1
        && cache == min)
    {
      pos = a;
      mini = video[a].size;
    }
  }
  if (mini != remain)
  {
    boola[pos] = 0;
    return mini;
  }
  return 0;
}

void print(std::vector<std::vector<int>> out)
{
  std::ofstream myfile("out1");
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

std::vector<std::vector<int>> fillcache(std::vector<Video> video, int size_cache, int nb_cache)
{
  ress vect = ress{};
  for (auto a = 0; a < nb_cache; a++)
    vect.push_back(std::vector<int>{});

  for (auto a = 0; a < (int)video.size(); a++)
    boola.push_back(1);

  std::vector<int> cap = std::vector<int>{};
  for (auto a = 0; a < nb_cache; a++)
    cap.push_back(size_cache);

  for (auto a = 0; a < nb_cache; a++)
  {
    int res = size_cache;
    pos = 0;
    while (res != 0)
    {
      res = best_size(video, cap[a], a);
      cap[a] -= res;
      if (res != 0)
      {
        vect[a].push_back(pos);
      }
    }
  }
  return vect;
}

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
  std::string endpoints;
  std::getline(iss_line, endpoints, ' ');
  int nb_endpoint = std::stoul(endpoints, nullptr, 10);
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

  print(fillcache(videos_vect, caches_size, nb_caches));
  return 0;
}
