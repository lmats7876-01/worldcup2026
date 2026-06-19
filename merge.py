import json
from datetime import datetime, timezone

with open('matches.json')   as f: matches   = json.load(f)
with open('standings.json') as f: standings = json.load(f)
with open('scorers.json')   as f: scorers   = json.load(f)
with open('news.json')      as f: news      = json.load(f)

out = {
    'updated':   datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'matches':   matches,
    'standings': standings,
    'scorers':   scorers,
    'news':      news
}

with open('data.json', 'w') as f:
    json.dump(out, f)

print('Written:', len(matches.get('matches', [])), 'matches,',
      len(news.get('articles', [])), 'articles')
