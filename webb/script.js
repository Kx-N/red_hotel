const x=5473;
let inout={};
// date picker range then post to database 
  $(function() {
    $('input[name="daterange"]').daterangepicker({
    opens: 'left'
    }, function(start, end, label) {
    console.log(start.format('DD-MM-YYYY') + ' to ' + end.format('DD-MM-YYYY'));
    cin = start.format('DD-MM-YYYY');
    cout = end.format('DD-MM-YYYY');

    fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      body: JSON.stringify({
        checkin: cin,
        checkout: cout,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
      .then((response) => response.json())
      .then((json) => console.log(json));

    });
  });

//   test fetch 
// fetch('http://2af725541272.ngrok. io/search_user_id?user=2', {
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