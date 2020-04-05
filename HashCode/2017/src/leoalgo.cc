#include "video.hh"
#include <vector>

using ress = std::vector<std::vector<int>>;

void sorting(std::vector<Video>& video)
{
  for (auto a = 0; a < (int)video.size(); a++)
  {
    for (auto b = 1; b < (int)video.size() - a; b++)
    {
      if (video[b].size < video[b - 1].size)
      {
        auto aux = video[b];
        video[b] = video[b - 1];
        video[b - 1] = aux;
      }
    }
  }
}

int best_size(std::vector<Video>& video, int remain, int& posf)
{
  int res = 0;
  int pos = 0;
  for (auto a = 0; a < (int)video.size(); a++)
  {
    if (remain - video[a].size >= 0 && remain - video[a].size < res)
    {
      pos = a;
      res = video[a].size - remain;
    }
  }
  if (res)
    video.erase(video.begin() + pos);
  posf = pos;
  return res;
}

void print(std::vector<std::vector<int>> out)
{
  std::ofstream myfile("out");
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
  sorting(video);

  std::vector<int> cap = std::vector<int>{};
  for (auto a = 0; a < nb_cache; a++)
    cap.push_back(100);

  for (auto a = 0; a < nb_cache; a++)
  {
    int res = size_cache;
    int pos = 0;
    while (res != 0)
    {
      res = best_size(video, cap[a], pos);
      cap[a] -= res;
      if (res)
        vect[a].push_back(pos);
    }
  }
  return vect;
}
