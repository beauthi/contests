#pragma once

#include <vector>

class Endpoint
{
  public:
    Endpoint(int dl, int nb_caches)
      : datacenter_latency(dl)
      , latency_vect(nb_caches)
    {}

    int datacenter_latency;
    std::vector<int> latency_vect;
};
