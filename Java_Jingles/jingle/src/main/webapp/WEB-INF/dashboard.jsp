<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
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
            <a href="/songs/add">Add a Song</a>
            <a href="/logout">Logout</a>
        </div>
    </nav>

    <div class="container mt-3">        
        <h1 class="text-center">Welcome ${loggedInUser.firstName} ${loggedInUser.lastName}</h1>

        <table class="table">
            <tr>
                <th>Song</th>
                <th>Album</th>
                <th>Artist</th>
                <th>Year</th>
                <th>Created By</th>
                <th>Likes</th>
                <th>Actions</th>
            </tr>
                <c:forEach items="${songs}" var="song">
                <tr>
                    <td><a href="/songs/${song.id}/view">${song.name}</a></td>
                    <td>${song.album}</td>
                    <td>${song.artist}</td>

                    <td><fmt:formatDate type ="date" value="${song.dateAdded}" pattern="yyyy"/></td>
                    <td>${song.user.firstName} ${song.user.lastName}</td>
                    <td>${song.usersLiked.size()}</td>
                    <td>

                        <c:choose>
                            <c:when test='${song.usersLiked.contains(loggedInUser)}'>
                                <a href="/songs/${song.id}/unlike">unlike</a>
                            </c:when>
                            <c:otherwise>
                                <a href="/songs/${song.id}/like">like</a>
                            </c:otherwise>
                        </c:choose>
                        
                        
                        <c:if test="${loggedInUser.id == song.user.id}">
                            <a href="/songs/${song.id}/edit">Edit</a>
                            <a href="/songs/${song.id}/delete">Delete</a>
                        </c:if>
                    </td>
                </tr>
                    
                </c:forEach>
        </table>
            

        <div class="border">

            <div>Top Ten Songs</div>
        </div>
    </div>


</body>
</html>