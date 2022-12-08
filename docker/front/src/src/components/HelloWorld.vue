<template>
    <div>
        <h1>Here is your tank datas !</h1>
        <form @submit="subForm">
            <div>
                <label for="minDate">Min Date</label>
                <input type="datetime-local" id="minDate" name="minDate" v-model="form.minDate">
            </div>
            <div>
                <label for="maxDate">Max Date</label>
                <input type="datetime-local" id="maxDate" name="maxDate" v-model="form.maxDate">
            </div>
            <div>
                <input type="submit" value="Submit">
            </div>
        </form>
        <div id="AllCanvas">
            <canvas id="myChartQte" width="100" height="100"></canvas>
            <canvas id="myChartPressure" width="100" height="100"></canvas>
            <canvas id="myChartLevel" width="100" height="100"></canvas>
        </div>
    </div>
</template>

<script>
import TankDataApi from "@/api/TankData";

import Chart from "chart.js/auto";
export default {
    name: 'HelloWorld',
    data() {
        return {
            chart: null,
            chartPressure: null,
            chartLevel: null,
            form: {
                minDate: null,
                maxDate: null
            }
        }
    },
    methods: {
        async subForm(e) {
            e.preventDefault();
            this.form.minDate = new Date(this.form.minDate);
            this.form.maxDate = new Date(this.form.maxDate);
            if (this.form.minDate > this.form.maxDate) {
                alert("Min date must be before max date");
                return;
            }
            console.log(this.form.minDate, this.form.maxDate);
            let min_date_obj = new Date(this.form.minDate);
            let max_date_obj = new Date(this.form.maxDate);
            let min_date = min_date_obj.getFullYear() + "-" + (min_date_obj.getMonth() + 1) + "-" + min_date_obj.getDate() + " " + min_date_obj.getHours() + ":" + min_date_obj.getMinutes() + ":" + min_date_obj.getSeconds();
            let max_date = max_date_obj.getFullYear() + "-" + (max_date_obj.getMonth() + 1) + "-" + max_date_obj.getDate() + " " + max_date_obj.getHours() + ":" + max_date_obj.getMinutes() + ":" + max_date_obj.getSeconds();
            this.chart.destroy();
            this.chartPressure.destroy();
            this.chartLevel.destroy();

            let data = (await TankDataApi.getAll(min_date, max_date)).data;
            let qte = data.map((item) => item.qte);
            let pressure = data.map((item) => item.pressure);
            let level = data.map((item) => item.level);
            let timestamp = data.map((item) => new Date(item.date));
            console.log("timestamp", timestamp);
            console.log("qte", qte);
            let ctx = document.getElementById('myChartQte');
            this.chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: timestamp,
                    datasets: [
                        {
                            label: "Water quantity",
                            data: qte,
                            borderColor: [
                                'rgba(0, 0, 0, 255)',
                            ],
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    xAxes: [{
                        type: 'time',
                        ticks: {
                            autoSkip: true,
                            maxTicksLimit: 2
                        }
                    }]
                }
            });
            ctx = document.getElementById('myChartPressure');
            this.chartPressure = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: timestamp,
                    datasets: [
                        {
                            label: "Water pressure",
                            data: pressure,
                            borderColor: [
                                'rgba(0, 0, 0, 255)',
                            ],
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    xAxes: [{
                        type: 'time',
                        ticks: {
                            autoSkip: true,
                            maxTicksLimit: 2
                        }
                    }]
                }
            });
            ctx = document.getElementById('myChartLevel');
            this.chartLevel = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: timestamp,
                    datasets: [
                        {
                            label: "Water Level",
                            data: level,
                            borderColor: [
                                'rgba(0, 0, 0, 255)',
                            ],
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    xAxes: [{
                        type: 'time',
                        ticks: {
                            autoSkip: true,
                            maxTicksLimit: 2
                        }
                    }]
                }
            });
        }
    },
    async mounted() {
        let data = (await TankDataApi.getAll()).data;
        let qte = data.map((item) => item.qte);
        let pressure = data.map((item) => item.pressure);
        let level = data.map((item) => item.level);
        let timestamp = data.map((item) => new Date(item.date));
        console.log("timestamp", timestamp);
        console.log("qte", qte);
        let ctx = document.getElementById('myChartQte');
        this.chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timestamp,
                datasets: [
                    {
                        label: "Water quantity",
                        data: qte,
                        borderColor: [
                            'rgba(0, 0, 0, 255)',
                        ],
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                xAxes: [{
                    type: 'time',
                    ticks: {
                        autoSkip: true,
                        maxTicksLimit: 2
                    }
                }]
            }
        });
        ctx = document.getElementById('myChartPressure');
        this.chartPressure = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timestamp,
                datasets: [
                    {
                        label: "Water pressure",
                        data: pressure,
                        borderColor: [
                            'rgba(0, 0, 0, 255)',
                        ],
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                xAxes: [{
                    type: 'time',
                    ticks: {
                        autoSkip: true,
                        maxTicksLimit: 2
                    }
                }]
            }
        });
        ctx = document.getElementById('myChartLevel');
        this.chartLevel = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timestamp,
                datasets: [
                    {
                        label: "Water Level",
                        data: level,
                        borderColor: [
                            'rgba(0, 0, 0, 255)',
                        ],
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                xAxes: [{
                    type: 'time',
                    ticks: {
                        autoSkip: true,
                        maxTicksLimit: 2
                    }
                }]
            }
        });
    },
    props: {
    }
}
</script>

<style scoped>
@import "HelloWorld.css";
</style>
