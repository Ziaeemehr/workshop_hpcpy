/* File: benchmark.h */

#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>

// Matrix-matrix multiplication (C = A * B)
// A: m x n matrix, B: n x p matrix, Result: m x p matrix
std::vector<std::vector<double>> matrix_multiply(const std::vector<std::vector<double>>& A,
                                                  const std::vector<std::vector<double>>& B) {
    int m = A.size();      // rows of A
    int n = A[0].size();   // cols of A (rows of B)
    int p = B[0].size();   // cols of B
    
    // Verify dimensions
    if ((int)B.size() != n) {
        throw std::invalid_argument("Matrix dimensions incompatible for multiplication");
    }
    
    // Initialize result matrix with zeros
    std::vector<std::vector<double>> C(m, std::vector<double>(p, 0.0));
    
    // Perform matrix multiplication
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            double sum = 0.0;
            for (int k = 0; k < n; k++) {
                sum += A[i][k] * B[k][j];
            }
            C[i][j] = sum;
        }
    }
    
    return C;
}
