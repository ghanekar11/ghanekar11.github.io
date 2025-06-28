var scripts = document.getElementsByTagName('script');
var myScript = scripts[scripts.length - 1];

var queryString = myScript.src.replace(/^[^\?]+\??/, '');

var params = parseQuery(queryString);

var recruit = 0;

// Should match topics in Keywords section in index html and json_to_html_per_pub


const topics_name_dict = {
  'Keypoint Tracking': 'Keypoint Tracking',
  'Dual-Pixel Sensors': 'Dual-Pixel Sensors',
  '3D Sensing': '3D Sensing',
  'Polarization': 'Polarization'
};

function parseQuery(query) {
    var Params = {};
    if (!query) return Params;
    var Pairs = query.split(/[;&]/);
    for (var i = 0; i < Pairs.length; i++) {
        var KeyVal = Pairs[i].split('=');
        if (!KeyVal || KeyVal.length != 2) continue;
        var key = unescape(KeyVal[0]);
        var val = unescape(KeyVal[1]);
        val = val.replace(/\+/g, ' ');
        Params[key] = val;
    }
    return Params;
}

function showPubs(id) {
  if (id == 0) {
    fetch('../pubs_selected.html')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('pubs').innerHTML = data;
                });
    // document.getElementById('pubs').innerHTML = document.getElementById('pubs_selected').innerHTML;
    document.getElementById('select0').style = 'text-decoration:underline;color:#000000';
    document.getElementById('select1').style = '';
    document.getElementById('select2').style = '';
    // Remove the keywords
    Object.keys(topics_name_dict).forEach(topic => {
      const element = document.getElementById(topic);
      if (element) { // Ensure the element exists
          element.style = '';
      } else {
          console.warn(`Element with ID '${topic}' not found.`);
      }
  });
  } else if (id == 1) {
    fetch('../pubs.html')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('pubs').innerHTML = data;
                });
    // document.getElementById('pubs').innerHTML = document.getElementById('pubs_by_date').innerHTML;
    document.getElementById('select1').style = 'text-decoration:underline;color:#000000';
    document.getElementById('select0').style = '';
    // Remove the keywords
    Object.keys(topics_name_dict).forEach(topic => {
      const element = document.getElementById(topic);
      if (element) { // Ensure the element exists
          element.style = '';
      } else {
          console.warn(`Element with ID '${topic}' not found.`);
      }
      });
  } else {
    // fetch('../pubs_by_topic.html')
    //             .then(response => response.text())
    //             .then(data => {
    //                 document.getElementById('pubs').innerHTML = data;
    //             });
    // // document.getElementById('pubs').innerHTML = document.getElementById('pubs_by_topic').innerHTML;
    // document.getElementById('select2').style = 'text-decoration:underline;color:#000000';
    // document.getElementById('select0').style = '';
    // document.getElementById('select1').style = '';
    // _altmetric_embed_init();
    fetch(`../pubs_by_topic_${id}.html`)
                .then(response => response.text())
                .then(data => {
                    document.getElementById('pubs').innerHTML = data;
                });
    // document.getElementById('pubs').innerHTML = document.getElementById('pubs_by_topic').innerHTML;
    document.getElementById('select2').style = 'text-decoration:underline;color:#000000';
    document.getElementById(id).style = 'text-decoration:underline;color:#000000';
    document.getElementById('select0').style = '';
    document.getElementById('select1').style = '';
    Object.keys(topics_name_dict).forEach(topic => {
      if (topic !== id){ // Remove underline from remaining id
      const element = document.getElementById(topic);
      if (element) { // Ensure the element exists
          element.style = '';
      } else {
          console.warn(`Element with ID '${topic}' not found.`);
      }
    }
      });
  }
}

function showRecruit() {
  if (recruit == 0) {
    document.getElementById('recruit').style='display:inline-block';
  } else {
    document.getElementById('recruit').style='display:none';
  }
  recruit = 1 - recruit;
}
