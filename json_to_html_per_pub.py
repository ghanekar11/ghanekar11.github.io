import json

# Load the corrected JSON data
with open('pubs.json', 'r', encoding='utf-8') as f:
    publications = json.load(f)

# Template for the HTML snippet with escaped curly braces
html_template_video = """
            <div class="row" onmouseout="{paper_id}_stop()" onmouseover="{paper_id}_start()" >
                <div class="col-md-2">
                    <div class="one">
                        <div class="two" id='{paper_id}_image'>
                            <a href="{link_1}" target="_blank">
                                <video width="160" height="160" muted autoplay loop>
                                    <source src='images/{paper_id}_after.{after_type}' type="video/{after_type}" >
                                    Your browser does not support the video tag.
                                </video>
                            </a>
                        </div>
                        <img src='images/{paper_id}_before.{before_type}' width="160" height="160" style="border-style: none" loading="lazy">
                    </div>
                    <script type="text/javascript">
                        function {paper_id}_start() {{
                            document.getElementById('{paper_id}_image').style.opacity = "1";
                        }}

                        function {paper_id}_stop() {{
                            document.getElementById('{paper_id}_image').style.opacity = "0";
                        }}
                        {paper_id}_stop()
                    </script>
                </div>
                <div class="col-md-9">
                    <div class="content-wrapper">
                        <div style="width:100%">
                            <span class="paper-title"><a target="_blank" href="{link_1}"> {title} </a></span><br>
                            {authors_html}
                            <br>
                            <div class="row">
                                <div class="col-sm-10">
                                    <font color="black"> {venue_full} <span class="venue">{venue_short}</span>, {venue_year}</font></a><br>
                                    <font style="font-size: 14px">
                                        {links_html}
                                    </font>
                                    {award_html}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <hr>
"""

html_template_image = """
            <div class="row" onmouseout="{paper_id}_stop()" onmouseover="{paper_id}_start()" >
                <div class="col-md-2">
                    <div class="one">
                        <div class="two" id='{paper_id}_image'>
                            <a href="{link_1}" target="_blank">
                                <img src='images/{paper_id}_after.{after_type}' width="160" height="160" style="border-style: none" loading="lazy">
                            </a>
                        </div>
                        <img src='images/{paper_id}_before.{before_type}' width="160" height="160" style="border-style: none" loading="lazy">
                    </div>
                    <script type="text/javascript">
                        function {paper_id}_start() {{
                            document.getElementById('{paper_id}_image').style.opacity = "1";
                        }}

                        function {paper_id}_stop() {{
                            document.getElementById('{paper_id}_image').style.opacity = "0";
                        }}
                        {paper_id}_stop()
                    </script>
                </div>
                <div class="col-md-9">
                    <div class="content-wrapper">
                        <div style="width:100%">
                            <span class="paper-title"><a target="_blank" href="{link_1}"> {title} </a></span><br>
                            {authors_html}
                            <br>
                            <div class="row">
                                <div class="col-sm-10">
                                    <font color="black"> {venue_full} <span class="venue">{venue_short}</span>, {venue_year}</font></a><br>
                                    <font style="font-size: 14px">
                                        {links_html}
                                    </font>
                                    {award_html}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <hr>
"""


# Helper function to format authors
def format_authors(authors):
    author_html = []
    for author, link in authors.items():
        if link == "bhargav":
            author_html.append(f'<span class="bhargav">{author}</span>')
        else:
            author_html.append(f'<span class="author"><a target="_blank" href="{link}">{author}</a></span>')
    return ", ".join(author_html)

# Helper function to format links
def format_links(links):
    link_html = []
    for name, url in links.items():
        if url:
            link_html.append(f'<a target="_blank" href="{url}">[{name}]</a>')
    return "&nbsp;•\n                                        ".join(link_html)

# Helper function to format awards
def format_award(award):
    if award['award title']:
        if award['award link']:
            return f'<span class="brsmall"></span><span class="highlight title"><a href="{award["award link"]}" target="_blank">{award["award title"]}</a></span><span class="highlight"> {award["award desc"]}</span><br>'
        else:
            return f'<span class="brsmall"></span><span class="highlight title">{award["award title"]}</span><span class="highlight"> {award["award desc"]}</span><br>'
    return ''

# Generate the HTML content
html_content = []
sel_html_content = []
year_html_dict = {}
topic_html_dict = {}

for paper_id, paper_info in publications.items():
    authors_html = format_authors(paper_info['authors'])
    links_html = format_links(paper_info['links'])
    # Use the first link available in the links dictionary as the project link
    project_link = next(iter(paper_info['links'].values()))
    title = paper_info['title']
    venue_full, venue_short, venue_year = paper_info['venue']
    before_type = paper_info['thumbnail']['before_type'].lower()
    after_type = paper_info['thumbnail']['after_type'].lower()
    award_html = format_award(paper_info['award'])
    
    # Use the first link available in the links dictionary as the link for the after_type video or image
    link_1 = next(iter(paper_info['links'].values()))

    if after_type == 'mp4':
        html_snippet = html_template_video.format(
            paper_id=paper_id,
            title=title,
            authors_html=authors_html,
            venue_full=venue_full,
            venue_short=venue_short,
            venue_year=venue_year,
            links_html=links_html,
            project_link=project_link,
            before_type=before_type,
            after_type=after_type,
            link_1=link_1,
            award_html=award_html
        )
    else:
        html_snippet = html_template_image.format(
            paper_id=paper_id,
            title=title,
            authors_html=authors_html,
            venue_full=venue_full,
            venue_short=venue_short,
            venue_year=venue_year,
            links_html=links_html,
            project_link=project_link,
            before_type=before_type,
            after_type=after_type,
            link_1=link_1,
            award_html=award_html
        )
    
    # For pubs
    html_content.append(html_snippet)
    # For pubs_selected
    if paper_info['highlight']:
        sel_html_content.append(html_snippet)
    # For pubs_by_date
    if not venue_year in year_html_dict.keys():
        year_html_dict[venue_year] = []
    year_html_dict[venue_year].append(html_snippet)
    # For pubs_by_topic
    for topic in paper_info['topics']:
        if not topic in topic_html_dict.keys():
            topic_html_dict[topic] = []
        topic_html_dict[topic].append(html_snippet)

# sel_html_content.insert(0,'<h6> Highlighted </h6>\n')

years = sorted(year_html_dict.keys(),reverse=True)
year_html_content = []
for year in years:
    # year_html_content.append(f'<div id={year}><h6>{year}</h6>\n')
    year_html_content.extend(year_html_dict[year])
    # year_html_content.append('</div>\n')

topics = topic_html_dict.keys()
topics_name_dict = {'Keypoint Tracking': 'Keypoint Tracking',
                    'Dual-Pixel Sensors': 'Dual-Pixel Sensors',
                    '3D Sensing': '3D Sensing',
                    'Polarization': 'Polarization'}
for topic in topics:
    topic_html_content = []
    topic_html_content.append(f'<div id={topic}_pubs><h6>{topics_name_dict[topic]}</h6>\n')
    topic_html_content.extend(topic_html_dict[topic])
    year_html_content.append('</div>\n')
    topic_html_content = "\n".join(topic_html_content)
    with open(f'pubs_by_topic_{topic}.html', 'w', encoding='utf-8') as f:
        f.write(topic_html_content)

from bs4 import BeautifulSoup
# Write the HTML content to a file
pubs_html_content = "\n".join(html_content)
with open('pubs.html', 'w', encoding='utf-8') as f:
    f.write(pubs_html_content)
sel_html_content = "\n".join(sel_html_content)
with open('pubs_selected.html', 'w', encoding='utf-8') as f:
    f.write(sel_html_content)
year_html_content = "\n".join(year_html_content)
with open('pubs_by_date.html', 'w', encoding='utf-8') as f:
    f.write(year_html_content)

# Update index.html
# Load the existing index.html
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find the div with id="pubs" and clear its content
pubs_div = soup.find('div', id='pubs')
if pubs_div:
    pubs_div.clear()
    new_hr = soup.new_tag("hr")
    new_hr['style'] = "margin-top:0.6em"
    pubs_div.append(new_hr)
    # Prettify the new content
    new_content = BeautifulSoup(pubs_html_content, 'html.parser').prettify()
    # Add the new content to the cleared pubs_div
    pubs_div.append(BeautifulSoup(new_content, 'html.parser'))

# Write the updated index.html back to the file without affecting the rest
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))