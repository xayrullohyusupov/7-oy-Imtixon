from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from dashboard.models import Xodim,Davomat
from .serializers import XodimSerializer
from django.utils import timezone

@api_view(['GET'])
def staff_list(request):
    xodimlar = Xodim.objects.all()
    serializer = XodimSerializer(xodimlar, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def attendance_create(request):
    xodim_id = request.data.get('id')
    if not xodim_id:
        return Response({'status': 'error', 'message': 'Xodim IDsi kiritilmagan.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        xodim = Xodim.objects.get(id=xodim_id)
        Davomat.objects.create(xodim=xodim, kelgan_vaqti=timezone.now())
        return Response({'status': 'success'})
    except Xodim.DoesNotExist:
        return Response({'status': 'error', 'message': 'Xodim topilmadi.'})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})
