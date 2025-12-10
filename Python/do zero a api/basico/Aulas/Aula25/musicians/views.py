from rest_framework.views import APIView
from rest_framework.response import Response
from musicians.models import Musician
from django.forms.models import model_to_dict


class MusicianView(APIView):
    
    
    def post(self, request):
        #aqui iremos pegar o objeto request.data, que se trata do body da requisição
        musician_data = request.data
        
        musician = Musician.objects.create(**musician_data)
        #acima estamos usando o unpacking ou seja ele ira quebrar o body nos parametros que temos na model para que o registro seja feito em banco
        """
            Podemos fazer as atribuições manualmente tambem dessa forma
            
            musician = Musician.objects.create(
                first_name  = musician_data['first_name'],
                last_name = musician_data['last_name'],
                instrument = musician_data['instrument'],
            )
            
            o processo acima é o processo 'manual' porem usando o unpacking se torna menos verboso
        """
        
        return Response(model_to_dict(musician), 201)
    
    def get(self, request):
        musicians = Musician.objects.all()
        
        musicians_dicts = []
        
        
        for musician in musicians:
            m = model_to_dict(musician)
            musicians_dicts.append(m)
            
        return Response(musicians_dicts)