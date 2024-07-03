// app.js
const holidays2024 = [
  '2024-01-01', '2024-01-08', '2024-03-25', '2024-03-28', '2024-03-29', 
  '2024-05-01', '2024-05-13', '2024-06-03', '2024-06-24', '2024-07-01', 
  '2024-07-20', '2024-08-07', '2024-08-19', '2024-10-14', '2024-11-04', 
  '2024-11-11', '2024-12-08', '2024-12-25'
];

const salarioMinimo2024 = 1300000; // Valor de ejemplo, ajustar según el salario real para 2024
const recargoDominicalFestivo = 1.75;
const recargoNocturno = 1.35;

function generateCalendar(year, month, startDay, endDay) {
  const calendar = document.getElementById('calendar');
  if (!calendar) return;

  const table = document.createElement('table');
  const headerRow = document.createElement('tr');
  ['Día', 'Fecha', 'Hora Ingreso', 'Hora Salida'].forEach(text => {
      const th = document.createElement('th');
      th.innerText = text;
      headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  for (let day = startDay; day <= endDay; day++) {
      const row = document.createElement('tr');
      const date = new Date(year, month, day);
      const dayOfWeek = date.getDay();
      const dateString = date.toISOString().split('T')[0];

      const dayCell = document.createElement('td');
      dayCell.innerText = day.toString();
      row.appendChild(dayCell);

      const dateCell = document.createElement('td');
      dateCell.innerText = dateString;
      row.appendChild(dateCell);

      const checkHoliday = holidays2024.includes(dateString);
      if (dayOfWeek === 0) {
          row.classList.add('sunday');
      }
      if (checkHoliday) {
          row.classList.add('holiday');
      }

      ['start', 'end'].forEach(type => {
          const inputCell = document.createElement('td');
          const input = document.createElement('input');
          input.type = 'time';
          input.classList.add(type);
          input.dataset.date = dateString;
          inputCell.appendChild(input);
          row.appendChild(inputCell);
      });

      table.appendChild(row);
  }

  calendar.appendChild(table);
}

function calculateTotal() {
  const rows = document.querySelectorAll('table tr');
  let total = 0;

  rows.forEach((row, index) => {
      if (index === 0) return; // Skip header row

      const inputs = row.querySelectorAll('input');
      const startInput = inputs[0];
      const endInput = inputs[1];

      const startTime = startInput.value;
      const endTime = endInput.value;
      if (!startTime || !endTime) return;

      const date = new Date(startInput.dataset.date);
      const dayOfWeek = date.getDay();
      const isHoliday = holidays2024.includes(date.toISOString().split('T')[0]);

      const startHour = parseInt(startTime.split(':')[0]);
      const endHour = parseInt(endTime.split(':')[0]);

      let dailyTotal = 0;
      for (let hour = startHour; hour < endHour; hour++) {
          if (hour >= 6 && hour < 22) {
              dailyTotal += salarioMinimo2024 / 240; // 240 hours per month
          } else {
              dailyTotal += (salarioMinimo2024 / 240) * recargoNocturno;
          }
      }

      if (dayOfWeek === 0 || isHoliday) {
          dailyTotal *= recargoDominicalFestivo;
      }

      total += dailyTotal;
  });

  const totalElement = document.getElementById('total');
  if (totalElement) {
      totalElement.innerText = `Total Salario: ${total.toFixed(2)}`;
  }
}

document.getElementById('calculate').addEventListener('click', calculateTotal);

generateCalendar(2024, 5, 16, 30); // Generar calendario desde el 16 de junio (mes 5) hasta el 30 de junio
