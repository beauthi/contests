CXX = clang++
CXXFLAGS = -std=c++14 -pedantic -Wall -Wextra -g

SRC = hashcode.cc
SRC := $(addprefix src/,$(SRC))
OBJS = $(SRC:.c=.o)
BIN = hashcode

.PHONY: all clean

all: $(OBJS)
	$(CXX) $(CXXFLAGS) -Isrc/ $(OBJS) -o $(BIN)

clean:
	@$(RM) $(BIN) *.out
