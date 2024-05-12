from operator import itemgetter

import requests
import plotly.express as px

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Response status: {r.status_code}")

submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:15]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        continue
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

article_links, comment_counts, hover_texts = [], [], []
for submission_dict in submission_dicts:
    title = submission_dict['title'][:35]
    discussion_link = submission_dict['hn_link']
    article_link = f'<a href="{discussion_link}"">{title}</a>'
    comment_count = submission_dict['comments']

    article_links.append(article_link)
    comment_counts.append(comment_count)
    hover_texts.append(submission_dict['title'])

title = "Active discussions on Hacker News"
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x=article_links, y=comment_counts, title=title, labels=labels,
        hover_name=hover_texts)

fig.update_layout(title_font_size=24, xaxis_title_font_size=18,
        yaxis_title_font_size=18)

fig.update_traces(marker_color='LightBlue', marker_opacity=0.7)

fig.show()