const x=5473;
var obj;
var room;
var type;
var price;
var dummy=[["6", "5", 7500],
["1", "1", 3000],
["7", "4", 5000],
["2", "2", 4000],
["4", "2", 4000],
["5", "1", 3000],
["10", "5", 7500],
["3", "3", 4500],
["9","4",5000]]
// date picker range then post to database 
  $(function() {
    $('input[name="daterange"]').daterangepicker({
    opens: 'left'
    }, function(start, end, label) {
    console.log(start.format('DD/MM/YYYY') + ' to ' + end.format('DD/MM/YYYY'));
    cin = start.format('DD/MM/YYYY');
    cout = end.format('DD/MM/YYYY');

    fetch('http://4755872ae47a.ngrok.io/search_av_room', {
      method: 'POST',
      body: JSON.stringify({
        "checkin": cin,
        "checkout": cout
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
      .then((response) => response.json())
      .then(data => obj = data)
      .then((json) => console.log(json));
      // end fetch

    });
  });

//   test fetch 
// fetch('http://2af725541272.ngrok.io/search_user_id?user=2', {
//   method: 'GET',
//   headers: {
//     'Content-type': 'application/json; charset=UTF-8',
//   },
// })
//   .then((response) => response.json())
//   .then((json) => console.log(json));

// get ok

// send payment 
function pay() {
fetch('URL', {
  method: 'POST',
  body: JSON.stringify({
    cusID : NUM,
    how : HOW,
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
}