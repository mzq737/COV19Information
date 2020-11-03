var ec_left1 = echarts.init(document.getElementById('l1'));

var ec_left1_Option = {
	title: {
		text: "",
		textStyle: {
		},
		left: 'left',
	},
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ["Cumulative Cases", "Cumulative Recovered", "Cumulative Deaths"],
		left: "right"
	},

	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		data: []
	}],
	yAxis: [{
		type: 'value',
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 12,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		axisLine: {
			show: true
		},
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
	}],
	series: [{
		name: "Cumulative Cases",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "Cumulative Recovered",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "Cumulative Deaths",
		type: 'line',
		smooth: true,
		data: []
	}]
};

ec_left1.setOption(ec_left1_Option)
