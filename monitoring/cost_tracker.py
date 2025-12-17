def estimate_cost(tokens, price_per_1k=0.002):
    return (tokens/1000) * price_per_1k