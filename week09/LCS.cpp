#include <iostream>
#include <string>

int LCS( std::string x, std::string y ) {
    int lenx = x.size();
    int leny = y.size();

    int matrix[lenx+1][leny+1];
    
    for( int i = 0; i < lenx; i++ ) {
        for( int j = 0; j < leny; j++ ) {
            if (i == 0 || j == 0) 
                matrix[i][j] = 0; 
  
            else if (x[i - 1] == y[j - 1]) 
                matrix[i][j] = matrix[i - 1][j - 1] + 1; 
  
            else
                matrix[i][j] = std::max(matrix[i - 1][j], matrix[i][j - 1]); 
        }
    }

    return matrix[lenx][leny];
}

int main( void ) {
    std::string str1 = "strive";
    std::string str2 = "hire";

    std::cout << LCS( str1, str2 ) << std::endl;
}