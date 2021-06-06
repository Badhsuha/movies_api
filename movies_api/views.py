import json
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
import datetime
from fpdf import FPDF

from .serializer import MovieSerielizer
from .models import Movies


class MoveisView(APIView):

    def post(self, request, *args, **kwargs):

            request.data['createdAt'] = datetime.datetime.utcnow()
            request.data['updateAt'] = datetime.datetime.utcnow()
            request.data['genres'] = json.dumps(request.data['genres'])
            serialized_data = MovieSerielizer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response("Movie Added", 200)
            else:
                return Response(serialized_data.errors, 401)

    def put(self, request, *args, **kwargs):
        errors = {}
        if request.data:
            request.data
            if 'id' not in request.data.keys():
                errors['id'] = 'Id required'
            if 'title' not in request.data.keys() and 'genres' not in request.data.keys():
                errors['nodata']='provide a data to update'
        else:
            errors['data_not_found'] = 'Pleas provide id and some data to update'
        if len(errors) > 0:
            return Response(errors, 401)

        try:
            data_to_update = {}
            movie = Movies.objects.get(id=request.data['id'])
            data_to_update['title'] = request.data.get('title', movie.title)
            data_to_update['genres'] = json.dumps(request.data.get('genres', movie.genres))
            movie.title = data_to_update['title']
            movie.genres = data_to_update['genres']
            movie.updateAt = datetime.datetime.utcnow()
            movie.save()
            return Response("movie updated", 200)
        except:
            return Response('Movie not found with id {0}'.format(request.data['id']), 401)


    def get(self, request, *args, **kwargs):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)

        movies = Movies.objects.order_by('-updateAt')
        dt = [{'id':movie.id, "title": movie.title, 'genres':json.loads(movie.genres), 'createdAt':movie.createdAt, 'updatedAt': movie.updateAt}  for movie in movies]

        line = 1
        for d in dt:
            pdf.cell(200, 10, txt = "id : {0}".format(d['id'])  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "title : {0}".format(d['title'])  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "genres : {0}".format(str(d['genres']))  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "CreatedAt : {0}".format(str(d['createdAt']))  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "UpdatedAt : {0}".format(str(d['updatedAt']))  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "----------------------"  ,ln = line)
            line += 1

        response = HttpResponse(pdf.output(dest='s').encode('latin-1'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format('movies.pdf')
        return response

    def delete(self, request, *args, **kwargs):

            if request.data:
                    if ('id' in request.data.keys()):
                        try:
                            movie = Movies.objects.get(id=request.data['id'])
                            movie.delete()
                            return Response('Movie removed', 200)
                        except:
                            return Response("movie not found with id {}".format(request.data['id']))
                    else:
                        return Response('Pleas provide id', 401)
            else:
                return Response('Pleas provide id', 401)


class GetMoviesByTitle(APIView):

    def get(self, request, *args, **kwargs):
        try:
         movie = Movies.objects.get(title=kwargs['title'])
         movie = {'title':movie.title,'genres':json.loads(movie.genres), 'createdAt':movie.createdAt, 'updateAt':movie.updateAt}
         return Response(movie, 200)
        except:
            return Response('No movis Found', 401)

class SearchMovie(APIView):

    def get(self, request, *args, **kwargs):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)

        movies = Movies.objects.all()
        search = kwargs['search']
        dt = [{'id':movie.id, "title": movie.title, 'genres':json.loads(movie.genres), 'createdAt':movie.createdAt, 'updatedAt': movie.updateAt}  for movie in movies]
        filtered_movies = filter(lambda x: all([ i in x['title'].lower() for i in search.split()]), dt)

        line = 1
        for d in filtered_movies:
            pdf.cell(200, 10, txt = "id : {0}".format(d['id'])  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "title : {0}".format(d['title'])  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "genres : {0}".format(str(d['genres']))  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "CreatedAt : {0}".format(str(d['createdAt']))  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "UpdatedAt : {0}".format(str(d['updatedAt']))  ,ln = line)
            line += 1
            pdf.cell(200, 10, txt = "----------------------"  ,ln = line)
            line += 1
        response = HttpResponse(pdf.output(dest='s').encode('latin-1'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format('movies.pdf')
        return response




