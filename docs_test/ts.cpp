#include <iostream> 

int main() 
{
    int i = 1; 
    int j = 3; 
    int k_i = i / j; 
    double k_d0 = i / j; 
    double k_d1 = 1.0 * i / j; 
    double k_d2 = static_cast<double>(i) / j; 

    std::cout << k_i << "," << k_d0 << "," << k_d1 << "," << k_d2 << std::endl; 


    std::cout << "hello python!" << std::endl; 
    std::cout << "111" << std::endl; 


    return 0;
}