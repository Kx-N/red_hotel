var obj=[["6", "5", 7500],
["1", "1", 3000],
["7", "4", 5000],
["2", "2", 4000],
["4", "2", 4000],
["5", "1", 3000],
["10", "5", 7500],
["3", "3", 4500],
["9","4",5000]];

let safe=5473;

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