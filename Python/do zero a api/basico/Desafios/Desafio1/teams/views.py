from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework import status


from kopa_do_mundo.utils import data_processing
from kopa_do_mundo.exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError

from .models import Team

class TeamsView(APIView):
    
    def post(self, request):
        
        team_data = request.data
        
        try:
            validated = data_processing(team_data)
            team = Team.objects.create(**validated)
            return Response(model_to_dict(team), 201)  
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({'error':err.message}, status=400)
        
        
    
    
    def get(self, request, team_id=None):
        
        if team_id:
            
            try:
                team  = Team.objects.get(pk = team_id)
            except Team.DoesNotExist:
                return Response({"message": "Team not found"}, 404)
        
            return Response(model_to_dict(team))
            
        else:
            teams = Team.objects.all()
            
            teams_dict = []
            
            for team in teams:
                teams_dict.append(model_to_dict(team))
            
            return Response(teams_dict)
        
  
    def delete(self, request, team_id):
          
        try:
            team  = Team.objects.get(pk = team_id)
            team.delete()
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
            
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
    def patch(self, request, team_id):
  
        try:
            team  = Team.objects.get(pk = team_id)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)   
        
        for field, value in request.data.items():
            setattr(team, field, value)
            
        team.save()
        
        return Response(model_to_dict(team), 200)
            
                      
            
