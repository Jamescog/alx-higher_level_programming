#!/usr/bin/node
myArr = process.argv.slice(2);
count = myArr.length;
if (count === 0){
	console.log('No argument');
}else{
	console.log(myArr[0])
}
