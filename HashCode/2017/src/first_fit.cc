#pragma once
#include <vector>
#include <video.hh>
#include <endpoint.hh>
#include <iostream>
#include <fstream>

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
      for (int k = 0; k < (int)e.size(); k++)
      {
        if (e[k].datacenter_latency > 0)
        {
          tmp.push_back(v[i].size);
          break;
        }
      }
      i++;
    }
    out.push_back(tmp);
  }
  return out;
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
