const x=5473;
// date picker range
  $(function() {
    $('input[name="daterange"]').daterangepicker({
      opens: 'left'
    }, function(start, end, label) {
      console.log(start.format('DD-MM-YYYY') + ' to ' + end.format('DD-MM-YYYY'));
      cin = start.format('DD-MM-YYYY');
      cout = end.format('DD-MM-YYYY');
    //   document.getElementById("demo").innerHTML = start.format('DD-MM-YYYY') +" to "+ end.format('DD-MM-YYYY');
    });
  });