async function moderate() {
  const token = document.getElementById('token').value;
  const fileInput = document.getElementById('file');
  if (!fileInput.files.length) return alert('Select a file!');
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  const res = await fetch('http://localhost:7000/moderate', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + token },
    body: formData
  });
  document.getElementById('result').textContent = await res.text();
} 