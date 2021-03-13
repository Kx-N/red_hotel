const x=5473;
let inout={};
// date picker range
  $(function() {
    $('input[name="daterange"]').daterangepicker({
    opens: 'left'
    }, function(start, end, label) {
    console.log(start.format('DD-MM-YYYY') + ' to ' + end.format('DD-MM-YYYY'));
    checkin = start.format('DD-MM-YYYY');
    checkout = end.format('DD-MM-YYYY');
    data={checkin,checkout};

    // fetch("url" , {
    // method:"POST",
    // body: JSON.stringify(data)
    // }).then(res => {
    //     console.log("Request complete! response:",res);
    // });

    //   document.getElementById("demo").innerHTML = start.format('DD-MM-YYYY') +" to "+ end.format('DD-MM-YYYY');
    });
  });