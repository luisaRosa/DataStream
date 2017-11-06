#include <iostream>
#include <random>
#include <chrono>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
#include <set>
#include <sstream> 
#include <string>
#include <ctime>
using namespace std;

long int MAX = 100000000000;
long int N = 100000000;

unsigned seed = 0;
default_random_engine generator(seed);	
uniform_real_distribution<double> distributionZ(0.0,1.0);
uniform_int_distribution<long int> distributionX(0,N);

unsigned long int step4(long int num_variables) {
	set<long int> samples;
	vector<pair<long int,int> > variables;

	int i = 0;
  	while(samples.size() < num_variables){
  		long int sample = distributionX(generator);
  		samples.insert(sample);
  		i++;
  	}
	// cada i sera um momento t, vejo se esse momento é uma das posicoes das minhas variaveis
	for(long int t=0;t<N;t++){
		//gero o numero
		double z = distributionZ(generator);
		double n = floor(1/(z*z));
		double number = (n<MAX) ? n : MAX;

		if(samples.count(t) > 0){
			variables.push_back(make_pair(number,1));
		}
		else {
			for (int index = 0; index<variables.size(); ++index){
				int element = variables[index].first;
				if(element==number){
					int value = variables[index].second;
					variables[index] = make_pair(number,value+1);
				}
			}
		}
	}
	unsigned long int ac = 0;
	for ( int c = 0; c < variables.size(); ++c ) {
		int value = variables[c].second;
		ac+= N*( (2*value)-1);
	}
	cout << "AC: " << ac << endl;
	cout << "variables size: " << variables.size() << endl;

	unsigned long int estimativa = ac/variables.size();

    cout << estimativa <<" second moment --estimado com "<< num_variables << " variaveis" << endl;
    return estimativa;
}	

unsigned long int step5(long int num_variables) {
	vector<pair<long int,int> > variables;

	for(long int t=0;t<N;t++){
		//gero o numero
		double z = distributionZ(generator);
		double n = floor(1/(z*z));
		double number = (n<MAX) ? n : MAX;

		if (t <= num_variables) {
			// Choose the first k times for k variables
			variables.push_back(make_pair(number,1));
		}
		if (t > num_variables) {
			// When the nth element arrives (n > k), choose it with probability k/n
			uniform_real_distribution<double> distributionKn(0.0,1.0);
			long int probability = distributionKn(generator);
			if (probability < num_variables / t) {
				// Choosen, throw one of the previously storedvariables X out, with equal probability
				variables.push_back(make_pair(number, 1));
				long int thrown = distributionKn(generator);
				variables.erase(variables.begin() + thrown -1);
			}
		}


		for (int index = 0; index<variables.size(); ++index){
			int element = variables[index].first;
			if(element==number){
				int value = variables[index].second;
				variables[index] = make_pair(number,value+1);
			}
		}
	}

	unsigned long int ac = 0;
	for ( int c = 0; c < variables.size(); ++c ) {
		int value = variables[c].second;
		ac+= N*( (2*value)-1);
	}
	cout << "AC: " << ac << endl;
	cout << "variables size: " << variables.size() << endl;

	unsigned long int estimativa = ac/variables.size();

    cout << estimativa <<" second moment --estimado com "<< num_variables << " variaveis" << endl;
    return estimativa;
}

int main() {
	step5(10);
	step5(20);
	step5(30);
	step5(40);
	step5(50);
	step5(100);
}
