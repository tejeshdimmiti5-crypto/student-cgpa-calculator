// Grade to Point mapping for JNTU
const gradePoints = {
    'S': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 0
};

// Sample subject data structure (you can expand this)
const subjects = {
    'JNTUK': {
        'R23': {
            'CSE': {
                '1': [
                    { name: 'Mathematics I', credits: 4 },
                    { name: 'Physics', credits: 3 },
                    { name: 'Chemistry', credits: 3 },
                    { name: 'English', credits: 2 },
                    { name: 'Computer Fundamentals', credits: 3 }
                ],
                '2': [
                    { name: 'Mathematics II', credits: 4 },
                    { name: 'Data Structures', credits: 4 },
                    { name: 'Digital Logic Design', credits: 3 },
                    { name: 'Environmental Science', credits: 2 }
                ]
            }
        }
    }
};

function continueApp() {
    const university = document.getElementById('university').value;
    const regulation = document.getElementById('regulation').value;
    const calculator = document.getElementById('calculator').value;
    
    alert(`Selected: ${university} - ${regulation} - ${calculator}\n\nThis feature will open the calculator page.`);
    // In a full app, you would navigate to calculator.html here
}

function loadSubjects() {
    let university = document.getElementById("university").value;
    let regulation = document.getElementById("regulation").value;
    let branch = document.getElementById("branch").value;
    let semester = document.getElementById("semester").value;

    // Check if data exists
    if (!subjects[university]?.[regulation]?.[branch]?.[semester]) {
        alert("Subjects data not available for this selection");
        return;
    }

    let list = subjects[university][regulation][branch][semester];
    let table = document.getElementById("subjectTable");

    table.innerHTML = `
        <tr>
            <th>Subject</th>
            <th>Credits</th>
            <th>Grade</th>
        </tr>
    `;

    list.forEach((sub, index) => {
        table.innerHTML += `
            <tr>
                <td>${sub.name}</td>
                <td>${sub.credits}</td>
                <td>
                    <select id="g${index}">
                        <option value="S">S</option>
                        <option value="A">A</option>
                        <option value="B">B</option>
                        <option value="C">C</option>
                        <option value="D">D</option>
                        <option value="E">E</option>
                        <option value="F">F</option>
                    </select>
                </td>
            </tr>
        `;
    });
}

function calculateSGPA() {
    let totalCredits = 0;
    let totalPoints = 0;

    const selects = document.querySelectorAll("select[id^='g']");
    selects.forEach((select, index) => {
        const grade = select.value;
        const row = select.closest('tr');
        const credits = parseInt(row.cells[1].textContent);
        
        totalCredits += credits;
        totalPoints += gradePoints[grade] * credits;
    });

    if (totalCredits === 0) return 0;
    return (totalPoints / totalCredits).toFixed(2);
}

function displayResult() {
    const sgpa = calculateSGPA();
    alert(`Your SGPA: ${sgpa}`);
}