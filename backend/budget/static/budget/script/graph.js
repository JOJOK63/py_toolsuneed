let ctx = document.getElementById('chart');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        datasets: [{
            label: "USD",
            data: [5, 1, 8, 12, 5, 1, 7, 2, 9, 5],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
            ]
        },
            {
                label: "EUR",
                data: [1, 7, 3, 4, 5, 6, 6, 8, 9, 5],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(201, 203, 207, 0.2)'
                ]
            }
        ]

    },
});