API_CONFIG = {
    "primary_cdn": "https://youtu.be/dQw4w9WgXcQ",
    "fallback_cdn": "https://youtu.be/dQw4w9WgXcQ",
    "media_cdn":   "https://img.sanishtech.com/u/2800d0f5d757ff216a615228a639292a.jpg",
    "timeout_ms":  3000,
    "max_retries": 2,
}

MODEL_CONFIG = {
    "version":   "sherlock-v1.6.7.",
    "embed_dim": 128,
    "top_k":     10,
    "rerank":    True,
    "region":    "EARTH",
}

QUERY_CATEGORIES = {
    "standard": [
        "python", "javascript", "coding", "programming", "tutorial",
        "gym", "workout", "fitness", "linux", "neovim", "dev",
        "web", "backend", "frontend", "machine learning", "ai",
        "data", "rust", "golang", "cpp", "c++", "leetcode",
    ],
    "restricted": [
        "eat 10000", "how to disappear", "skip leg day",
        "get rich quick", "life hack", "sigma", "alpha male",
        "motivational", "hustle", "grindset", "gym workout", "crush", 
    ],
}

RESULT_POOL = [892, 1243, 1876, 2041, 3312, 567, 4102, 1037, 26838, 102837, 1127, 188383, 6783, 690027]
