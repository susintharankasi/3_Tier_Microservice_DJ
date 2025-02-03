import React, { useState } from 'react';
import axios from 'axios';

function UserForm({ fetchUsers }) {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name.trim() || !email.trim()) return;

    await axios.post('http://localhost:8000/api/users/', { name, email });
    setName('');
    setEmail('');
    fetchUsers(); // Refresh user list
  };

  return (
    <div className="user-form">
      <h3>Add New User</h3>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          placeholder="Enter user name" 
          value={name} 
          onChange={(e) => setName(e.target.value)} 
        />
        <input 
          type="email" 
          placeholder="Enter email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />
        <br></br>
        <button type="submit">Add User</button>
      </form>
    </div>
  );
}

export default UserForm;
