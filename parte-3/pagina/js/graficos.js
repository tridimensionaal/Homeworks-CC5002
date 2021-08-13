function error(g1, n){
    div = document.getElementById(g1);
    div.innerHTML = "<h4> Ocurrió un error al cargar el gráfico " + n + "</h4>";
}

function g1(){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '../cgi-bin/g1.py', true); 
    xhr.timeout = 1000;
    xhr.responseType = "json";
    xhr.onload = function(){
        let values = xhr.response;
        Highcharts.chart('g1', {
          chart: {
            type: 'line'
          },
          title: {
            text: 'Cantidad de avistamientos por día'
          },
          xAxis: {
            categories: values["fechas"]
          },
          yAxis: {
              title: {
                  text: 'Cantidad de avistamientos'
              }
          },
          plotOptions: {
              line: {
                  dataLabels: {
                      enabled: true
                  },
                  enableMouseTracking: false
              }
          },
          series: [{
              name: 'Avistamientos por día',
              data: values["values"]
          }]
        });
    }
    xhr.onerror = error('g1', 1);
    xhr.send();
}

function g2(){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '../cgi-bin/g2.py', true); 
    xhr.timeout = 1000;
    xhr.responseType = "json";
    xhr.onload = function(){
        let values = xhr.response;
        Highcharts.chart('g2', {
          chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Porcentaje de avistamientos por tipo'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        accessibility: {
            point: {
                valueSuffix: '%'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            }
        },
        series: [{
            name: 'Porcentaje',
            colorByPoint: true,
            data: [{
                name: 'Insecto',
                y: values[0],
                sliced: true,
                selected: true
            }, {
                name: 'Arácnido',
                y: values[1]
            }, {
                name: 'Miriápodo',
                y: values[2]
            }, {
                name: 'No identificado',
                y: values[3]

            }]
        }]
        });
     
        }
    xhr.onerror = error('g2', 2);
    xhr.send();
}

function g3(){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '../cgi-bin/g3.py', true); 
    xhr.timeout = 1000;
    xhr.responseType = "json";
    xhr.onload = function(){
        let values = xhr.response;
        Highcharts.chart('g3', {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Cantidad de avistamientos por tipo para todos los meses del año'
            },
            xAxis: {
                categories: [
                    'Ene',
                    'Feb',
                    'Mar',
                    'Apr',
                    'May',
                    'Jun',
                    'Jul',
                    'Ago',
                    'Sep',
                    'Oct',
                    'Nov',
                    'Dec'
                ],
                crosshair: true
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Cantidad de avistamientos'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: 'Vivo',
                data: values["vivos"]
            }, {
                name: 'Muerto',
                data: values["muertos"]
            }, {
                name: 'Estado no identificado',
                data: values["no sé"]
            }]
        });
    }
    xhr.onerror = error('g3', 3);
    xhr.send();
}





