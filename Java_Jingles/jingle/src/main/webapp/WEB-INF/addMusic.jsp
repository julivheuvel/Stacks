<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form" %>
<%@ page isErrorPage="true" %>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <title>Java Jingles</title>
</head>
<body>
    
    <nav class="container d-flex justify-content-between mt-3">
        <div>
        </div>
        <div>
            <a href="/dashboard">Dashboard</a>
            <a href="/logout">Logout</a>
        </div>
    </nav>

    <div class="container border mt-3">        
        <h1 class="text-center border">Add Music</h1>
		<p class = "text-center text-danger">${notAllowed}</p>
        <form:form method="POST" action="/songs/new" modelAttribute="newSong">
	        <p>
	            <form:label path="name">Name:</form:label>
	            <form:errors path="name"/>
	            <form:input path="name"/>
	        </p>
	        <p>
	            <form:label path="album">Album:</form:label>
	            <form:errors path="album"/>
	            <form:input path="album"/>
	        </p>
	        <p>
	            <form:label path="artist">Artist:</form:label>
	            <form:errors path="artist"/>
	            <form:input path="artist"/>
	        </p>
	        <p>
	            <form:label path="dateAdded">Date Created:</form:label>
	            <form:errors path="dateAdded"/>
	            <form:input type="date" path="dateAdded"/>
	        </p>
	        <input type="submit" value="Add It!"/>
	    </form:form>
    </div>
</body>
</html>