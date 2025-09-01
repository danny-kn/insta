# Instagram Data Processing and Analysis

In this project, I implement an Instagram data processing system in Python that analyzes exported Instagram data to generate CSV reports and identify follower relationship patterns. The program uses type-safe data processing mechanisms with robust error handling to parse JSON exports and produce clean, structured output.

## Usage

**Data Preparation:**

Place your Instagram data export files in the following structure:
```
data/connections/followers_and_following/
├── followers.json
├── following.json
└── pending_follow_requests.json
```

**Execution:**

Run the program:
```bash
python3 src/insta.py
```

**Program Output:**

The script processes all data types and displays counts:
```bash
followers: 1000
following: 1250
pending follow requests: 50
not following back: 380
```

**Generated Files:**

CSV files are created in the `output/` directory:
- `followers.csv`: Complete followers list
- `following.csv`: Complete following list
- `pending_follow_requests.csv`: Pending follow requests
- `not_following_back.csv`: Users you follow who don't follow back

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
