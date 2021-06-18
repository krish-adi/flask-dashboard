window.chartColors = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
};

Chart.Legend.prototype.afterFit = function() {
	this.height = this.height + 5;
};

var randomScalingFactor = function() {
	return Math.round(Math.random() * 100);
};

var chartColors = window.chartColors;
var COLORS = ['#4dc9f6', '#f67019', '#f53794', '#537bc4', '#acc236', '#166a8f', '#00a950', '#58595b', '#8549ba'];
var color = Chart.helpers.color;
