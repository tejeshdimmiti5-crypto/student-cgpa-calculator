function getGradePoint(grade){

    if(grade=="O") return 10;
    if(grade=="A+") return 9;
    if(grade=="A") return 8;
    if(grade=="B+") return 7;
    if(grade=="B") return 6;
    if(grade=="C") return 5;

    return 0;
}

function calculateSGPA(){

    let credits=[
        Number(document.getElementById("c1").value),
        Number(document.getElementById("c2").value),
        Number(document.getElementById("c3").value)
    ];

    let grades=[
        document.getElementById("g1").value,
        document.getElementById("g2").value,
        document.getElementById("g3").value
    ];

    let totalCredits=0;
    let totalCreditPoints=0;

    for(let i=0;i<3;i++){

        totalCredits+=credits[i];

        totalCreditPoints+=credits[i]*getGradePoint(grades[i]);

    }

    let sgpa=(totalCreditPoints/totalCredits).toFixed(2);

    let percentage=(sgpa*9.5).toFixed(2);

    document.getElementById("result").innerHTML=
    `
    <h3>Result</h3>

    Total Credits : ${totalCredits}<br><br>

    Total Credit Points : ${totalCreditPoints}<br><br>

    SGPA : ${sgpa}<br><br>

    Percentage : ${percentage}%
    `;
}
