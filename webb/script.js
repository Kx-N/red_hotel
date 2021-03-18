const x=5473;
var obj;
var payment;
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
["9","4",5000]];
// date picker range then post to database 
  $(function() {
    $('input[name="daterange"]').daterangepicker({
    opens: 'left'
    }, function(start, end, label) {
    console.log(start.format('DD/MM/YYYY') + ' to ' + end.format('DD/MM/YYYY'));
    cin = start.format('DD/MM/YYYY');
    cout = end.format('DD/MM/YYYY');

    fetch('http://192.168.1.38:5000/search_av_room', {
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
      //create talble
      function createTable(tableData) {
        var table = document.createElement('table');
        var tableBody = document.createElement('tbody');
      
        tableData.forEach(function(rowData) {
          var row = document.createElement('tr');
      
          rowData.forEach(function(cellData) {
            var cell = document.createElement('td');
            cell.appendChild(document.createTextNode(cellData));
            row.appendChild(cell);
          });
      
          tableBody.appendChild(row);
        });
      
        table.appendChild(tableBody);
        document.body.appendChild(table);
      }
      
      createTable(obj);
      // 

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


const myform = document.getElementById('myform');

myform.addEventListener('submit',function(e) {
  e.preventDefault();
  const formdata = new FormData(this);

  fetch('http://192.168.1.38:5000/dummy',{
    method:'post',
    body: formdata
  }).then(console.log(x))
  .then(function (response){
    return response.text();
  }).then(function (text) {
    console.log(text);
  }).catch(function (error) {
    console.error(error);
  })

});


document.querySelector('form.form').addEventListener('submit', function(e) {
  e.preventDefault();
  let x = document.querySelector('form.form').elements;
  console.log("room", x['room'].value);
  console.log("driver", x['driver'].value);
  console.log("massage", x['massage'].value);
  console.log("breakfast", x['breakfast'].value);
  console.log("dinner", x['dinner'].value);
  console.log("firstname", x['fname'].value);
  console.log("lastname", x['lname'].value);
  console.log("gender", x['gender'].value);
  console.log("age", x['age'].value);
  console.log("email", x['email'].value);
  console.log("telephone", x['telephone'].value);

});