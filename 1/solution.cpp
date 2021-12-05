#include <iostream>
#include <fstream>
#include <vector>


std::vector<int> getInput(std::string& filename) {

	std::ifstream stream(filename); 
	std::vector<int> input; 
	std::string line; 
	while(std::getline(stream, line))
	{
		input.push_back(std::stoi(line));
	}
	return input; 
}

int calculateDepth(std::vector<int>& input) {

	auto depth = 0;
	auto currentSum = 0;
	auto previousSum = 0; 
	for(int i = 0; i < input.size(); ++i)
	{
		if( (i + 2) < input.size())
		{
			currentSum = 0;
			for(int j = i; j < (i + 3); ++j)
			{

				currentSum += input[j]; 
			}

			if(previousSum < currentSum)
			{
				depth++; 
			}
			previousSum = currentSum;
		}
	}
	return depth - 1; 
}

auto main() -> int {

	std::string filename = "input.txt"; 
	auto input = getInput(filename); 
	auto result = calculateDepth(input);
	//auto result = 0; 
	std::cout<<"Result: "<< result << std::endl; 
	return 0;
}