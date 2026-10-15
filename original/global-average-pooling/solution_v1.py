def global_average_pooling(X):
    """Compute channel-wise spatial averages for an NCHW 4D nested list."""
    N = len(X)
    C = len(X[0])
    H = len(X[0][0])
    W = len(X[0][0][0])
    result = []
    for n in range(N):
        avg_vector = []
        for c in range(C):
            total = 0
            for h in range(H):
                for w in range(W):
                    total += X[n][c][h][w]
            avg_vector.append(total / (H * W))
        result.append(avg_vector)
    return result


if __name__ == "__main__":
    X = [[[[1, 2], [3, 4]], [[2, 4], [6, 8]]]]
    assert global_average_pooling(X) == [[2.5, 5.0]]
    print(global_average_pooling(X))
