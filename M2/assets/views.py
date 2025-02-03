from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.timezone import now
from .models import Asset, AuditLog
from .serializers import AssetSerializer, AuditLogSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        """ Assign asset to a user """
        asset = self.get_object()
        user_id = request.data.get('user_id')
        if user_id:
            asset.assigned_to_id = user_id
            asset.save()
            AuditLog.objects.create(asset=asset, user=request.user, action=f"Assigned to {request.user.username}")
            return Response({'message': 'Asset assigned successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def decommission(self, request, pk=None):
        """ Decommission an asset """
        asset = self.get_object()
        asset.status = 'Decommissioned'
        asset.save()
        AuditLog.objects.create(asset=asset, user=request.user, action="Decommissioned")
        return Response({'message': 'Asset decommissioned'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def expiring_licenses(self, request):
        """ Get all licenses expiring in the next 7 days """
        upcoming_expiry = now().date()
        expiring_assets = Asset.objects.filter(expiry_date__lte=upcoming_expiry)
        serializer = self.get_serializer(expiring_assets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all().order_by('-timestamp')
    serializer_class = AuditLogSerializer

