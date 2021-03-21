const x=5473;
const nowday="19/03/2021"
var obj;
var booking;
var price;
var dummy2=["https://92.168.1.38:5000/prompt_pay?book_id=20&met = cash",
"https://92.168.1.38:5000/prompt_pay?book_id=20&met = visa",
"https://92.168.1.38:5000/prompt_pay?book_id=20&met = mastercard",
"https://92.168.1.38:5000/prompt_pay?book_id=20&met = bitcoin"];
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

    // fetch('http://192.168.1.38:5000/search_av_room', {
    fetch('url', {

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
      dummy.unshift(["RoomID","Type","Price/Night"]);
      createTable(dummy);

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
  .then(data => booking = data)
  .then((json) => console.log(json));
}


// const myform = document.getElementById('myform');

// myform.addEventListener('submit',function(e) {
//   e.preventDefault();
//   const formdata = new FormData(this);



function handleFormSubmit(event) {
  event.preventDefault();

  document.getElementById("bookdate").value = nowday;
  document.getElementById("checkin").value = cin;
  document.getElementById("checkout").value = cout;

  var checkboxes = document.getElementsByTagName('input');

  if(document.getElementById("driver").checked) {
    document.getElementById('undriver').disabled = true;
  }
  if(document.getElementById("massage").checked) {
    document.getElementById('unmassage').disabled = true;
  }
  if(document.getElementById("breakfast").checked) {
    document.getElementById('unbreakfast').disabled = true;
  }
  if(document.getElementById("dinner").checked) {
    document.getElementById('undinner').disabled = true;
  }
  
  const data = new FormData(event.target);
  
  const formJSON = Object.fromEntries(data.entries());

  // formJSON.roomid = data.getAll('roomid');
  // formJSON.person = data.getAll('person');


  //fetch in
  const results = document.querySelector('.results pre');
  results.innerText = JSON.stringify(formJSON, null, 2);

  // fetch('http://192.168.1.38:5000/create_booking', {
  fetch('url', {

      method: 'POST',
      body: JSON.stringify(formJSON, null, 2),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
      .then((response) => response.json())
      .then(data => booking = data)
      .then((json) => console.log(json));




      // document.getElementById('boximage').style.display = "block";
      document.getElementById('cash').href=dummy2[0];
      document.getElementById('mastercard').href=dummy2[2];
      document.getElementById('visa').href=dummy2[1];
      document.getElementById('btc').href=dummy2[3];

      if ($('#boximage').css('opacity') == 0) {
        $('#boximage').css('opacity', 1);

    }
    else {
        $('#boximage').css('opacity', 0);
    }

    
    // setTimeout("alertWelcome();",5000);
    $('a').click( function(e) {
      e.preventDefault(); 
      alert ("Successful payment"); return false; } );


}

const form = document.querySelector('.box2');
form.addEventListener('submit', handleFormSubmit);
// =============================================




function myFunction() {
  var x = document.getElementById("type");
  if ($('#type').css('opacity') == 0) {
    $('#type').css('opacity', 1);}
  else {
    $('#type').css('opacity', 0);}
}