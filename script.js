function loadSubjects(){

document.getElementById("subjects").innerHTML=`

<table border="1" width="100%">

<tr>
<th>Subject</th>
<th>Credits</th>
<th>Grade</th>
</tr>

<tr>
<td>Programming</td>
<td>3</td>
<td>
<select>
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

<tr>
<td>Mathematics</td>
<td>4</td>
<td>
<select>
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

<tr>
<td>Physics</td>
<td>3</td>
<td>
<select>
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

</table>

<br>

<button onclick="alert('Next we will calculate SGPA')">
Calculate SGPA
</button>

`;

}
