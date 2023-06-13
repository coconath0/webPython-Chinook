<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style>
    html * {
      font-family: 'Playfair', serif;
    }
    body {
      background-color: #faf5f7;
    }
    
    h1 {
      color: #b5768e;
      text-align: center;
    }
    h2{
      color:#c46c8e;
    }
    a{
      color: #854468;
      text-decoration: none;
      padding: 5px;
    }

    ul {
      list-style-type: none;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background-color: #e8cad6;
    }
    
    li {
      float: left;
    }
    
    li a {
      display: block;
      color: white;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
    }
    
    li a:hover:not(.active) {
      background-color: #e0bccb;
    }
    
    .active {
      background-color: #b5768e;
    }

    .center{
    margin-left: auto;
    margin-right: auto;
    }

    th {
      background-color: #fff3b8; /* Pastel yellow */
      padding: 10px;
    }
    
    td {
      text-align: center;
      padding: 10px;
      background-color: #fce1eb; /* Pastel orange */
    }

    footer {
      background-color: #945177; /* Pastel pink */
      padding: 10px;
      text-align: center;
      color: #fff9db; /* Pastel yellow */
    }

    .btn{
      background-color: #b5768e;
      border:none;
      border-radius: 8px;
      color: white;
      padding: 12px 20px;
      text-align: center;
      font-size: 12px;
      margin: 5px 2px;
      opacity: 0.5;
      transition: 0.3s;
      display: inline-block;
      text-decoration: none;
      cursor: pointer;
      margin-left: auto;
      margin-right: auto;
    }
    .btn:hover{
      opacity:1;
    }

    label{
    color: #854468;
    font-weight: bold;
    }
    p{
      color: #ffffff;
    }
    h3{
      color: #854468;
    }
    input{
    padding: 3px;
    font-size: 14px;
    font-weight: 600;
    width: 300px;
    }
  </style>
</head>