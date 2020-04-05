#pragma once

#include <vector>

class Video
{
  public:
    Video(int s, int endpoints)
      : size(s)
      , end(endpoints)
    {
    }
    int size;
    std::vector<long> end;
};
