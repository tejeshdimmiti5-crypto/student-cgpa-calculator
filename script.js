
function loadSubjects(){

let university=document.getElementById("university").value;

let regulation=document.getElementById("regulation").value;

let branch=document.getElementById("branch").value;

let semester=document.getElementById("semester").value;

let list=subjects[university][regulation][branch][semester];

let table=document.getElementById("subjectTable");

table.innerHTML="";

table.innerHTML=`

<tr>

<th>Subject</th>

<th>Credits</th>

<th>Grade</th>

</tr>

`;

list.forEach((sub,index)=>{

table.innerHTML+=`

<tr>

<td>${sub.name}</td>

<td>${sub.credits}</td>

<td>

<select id="g${index}">

<option>S</option>

<option>A</option>

<option>B</option>

<option>C</option>

<option>D</option>

<option>E</option>

<option>F</option>

</select>

</td>

</tr>

`;

});

}
