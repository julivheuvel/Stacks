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
        <div></div>
        <div>
            <a href="/dashboard">Dashboard</a>
            <a href="/logout">Logout</a>
        </div>
    </nav>

    <div class="container border mt-3">        
        <h1 class="text-center border">Update ${song.name}</h1>
		<p class = "text-center text-danger">${notAllowed}</p>

		<form:form action="/songs/${song.id}/update" method="PUT" modelAttribute="song">
			<p>
	            <form:errors class="text-danger" path="name"/>
	            <div>
					<form:label path="name">Name:</form:label>
					<form:input path="name"/>
				</div>
	        </p>
	        <p>
	            <form:errors class="text-danger" path="album"/>
	            <div>
					<form:label path="album">Album:</form:label>
					<form:input path="album"/>
				</div>
	        </p>
	        <p>
	            <form:errors class="text-danger" path="artist"/>
	            <div>
					<form:label path="artist">Artist:</form:label>
					<form:input path="artist"/>
				</div>
	        </p>
	        <p>
	            <form:errors class="text-danger" path="dateAdded"/>
	            <div>
					<form:label path="dateAdded">Date Created:</form:label>
					<form:input type="date" path="dateAdded"/>
				</div>
	        </p>
	        <form:hidden path="user" />
	        <input type="submit" value="Update It!"/>
		</form:form>

		
    </div>

</body>
</html>