import unreal
@unreal.uclass()
class GlobalEditorUtilityBase(unreal.GlobalEditorUtilityBase):pass

utilBase = GlobalEditorUtilityBase()
assetList = utilBase.get_selected_assets()

for asset in assetList:
    prefix = ''
    asset_type = type(asset)
    if asset_type ==unreal.StaticMesh:
        prefix = 'SM'
    if asset_type == unreal.Material:
        prefix = 'M'
    if asset_type == unreal.SkeletalMesh:
        prefix = 'SK'
    if prefix =='':
        continue
    utilBase.rename_asset(asset,'{}_{}'.format(prefix,asset.get_name()))