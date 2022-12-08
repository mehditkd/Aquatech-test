<h3 align="center">Aquatest</h3>

---

<p align="center"> Simulating and reporting water tank data
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This project is a test from Aquatech company.
I must simulating datas from a water tank that have 3 sensor,
- Water Pressure (bar)
- Water Level (cm)
- Water Volume (L)

those values must describe a water tank with his consumption.
Due to lack of time because of a busy schedule, I couldn't finish the way I wanted to.

## 🏁 Getting Started <a name = "getting_started"></a>

In this repository you will see 4 main folders :
- gen -> the gen folder contains all the python script that's necessary to create dataset
- schema -> Just basic sql schema to store values
- scripts -> Scripting to install, launch and generate datas
- site -> Containing website files (splitted in two folder backend and frontend) to see the datas in graph

### Prerequisites

You need all this technologies to launch all the functionnalities

- Mariadb15.1+ (or Mysql)
- Python3.9+ (and pip3 obviously)
- VueJs5.0.4+

### Installing

To install programs you can launch all bash scripts in ./scripts folder that begin with install.
- ./scripts/install_back.sh
- ./scripts/install_front.sh
- ./scripts/install_generator.sh
- ./scripts/install_db.sh
- ./scripts/install_all.sh

### Usage

You can launch and use programs with bash scripts in ./scripts folder

## ⛏️ Built Using <a name = "built_using"></a>

This is the list of technologies that's used and why

- MariaDB: I used MariaDB because it's a good SQL technology, I think that the best technology for this is timestamp orientend database likes InfluxDB, but due to lack of times I couldn't learn it.
- Flask: Flask is a python library to create simply API, for this test I didn't need powerful or complex API and backend technologies so it's ok. But even if python can manage likes 30k or 50k informations, I perfectly know that it's not a really good technology for real usage with hundreds of thousands of data.
- VueJS: Vuejs is the framework that I used for frontend development, it's the frontend technologies that I know the best. It's simple and useful.
- ChartJS: CharJs is a lib that I discovered with this project, it can create charts with data to display. But the main defect is that CharJs cannot handle thousands of data and I didn't know until I tried to use functionalities likes filter. The library is crashing because it uses recursive functions and with those thousands of datas it overflows.

So to resume my choices, I perfectly know that's not perfect and that must be upgraded for real usage but in the current context it works fine. It's just a test for a company. If I will retry, I will take time to learn better technologies and use them in the right way.

## ✍️ Authors <a name = "authors"></a>

- [@mehditkd](https://github.com/mehditkd)