"""
#######################################################################

CCPN Data Model version 2.1.2

Autogenerated by PyXmlMapWrite revision 1.29 on Mon Mar  2 17:24:11 2015
  from data model element molsim.Symmetry revision ?

#######################################################################
======================COPYRIGHT/LICENSE START==========================

Symmetry.py: python XML-I/O-mapping for CCPN data model, MetaPackage molsim.Symmetry

Copyright (C) 2007  (CCPN Project)

=======================================================================

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
 
A copy of this license can be found in ../../../license/LGPL.license
 
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.
 
You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


======================COPYRIGHT/LICENSE END============================

for further information, please contact :

- CCPN website (http://www.ccpn.ac.uk/)

- email: ccpn@bioc.cam.ac.uk

=======================================================================

If you are using this software for academic purposes, we suggest
quoting the following references:

===========================REFERENCE START=============================
Rasmus H. Fogh, Wayne Boucher, Wim F. Vranken, Anne
Pajon, Tim J. Stevens, T.N. Bhat, John Westbrook, John M.C. Ionides and
Ernest D. Laue (2005). A framework for scientific data modeling and automated
software development. Bioinformatics 21, 1678-1684.


This file was generated with the Memops software generation framework,
and contains original contributions embedded in the framework

===========================REFERENCE END===============================
"""
from memops.general.Constants import baseDataTypeModule as basicDataTypes
# 
#  Current package api
import molsim.api.Symmetry

def makeMapping(globalMap):
  """
  generates XML I/O mapping for package SYMM, adding it to globalMap
  """
  
  from memops.xml.Implementation import bool2str, str2bool

  # Set up top level dictionaries
  loadMaps = globalMap.get('loadMaps')
  mapsByGuid = globalMap.get('mapsByGuid')

  abstractTypes = globalMap.get('SYMM').get('abstractTypes')
  exolinks = globalMap.get('SYMM').get('exolinks')

  # DataType SymmetryOpCode
  currentMap = {}
  abstractTypes['SymmetryOpCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00006'] = currentMap
  loadMaps['SYMM.SymmetryOpCode'] = currentMap
  currentMap['tag'] = 'SYMM.SymmetryOpCode'
  currentMap['type'] = 'simple'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00006'
  currentMap['toStr'] = 'text'
  currentMap['cnvrt'] = 'text'

  # Class MolSystemSymmetrySet
  currentMap = {}
  abstractTypes['MolSystemSymmetrySet'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00001'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00001'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'molSystemSymmetrySets'
  currentMap['isTop'] = True
  currentMap['class'] = molsim.api.Symmetry.MolSystemSymmetrySet
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute MolSystemSymmetrySet.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute MolSystemSymmetrySet.createdBy
  contentMap['createdBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00002__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute MolSystemSymmetrySet.details
  currentMap = {}
  contentMap['details'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-08-05-11:53:29_00002'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.details'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.details'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-08-05-11:53:29_00002'
  currentMap['name'] = 'details'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00036')

  # Attribute MolSystemSymmetrySet.guid
  contentMap['guid'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:26_00002')

  # Attribute MolSystemSymmetrySet.isModifiable
  contentMap['isModifiable'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-17-14:16:26_00010__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute MolSystemSymmetrySet.lastUnlockedBy
  contentMap['lastUnlockedBy'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:00:59_00003__www.ccpn.ac.uk_Fogh_2007-10-03-14:53:27_00001__www.ccpn.ac.uk_Fogh_2006-09-14-16:28:57_00002')

  # Attribute MolSystemSymmetrySet.name
  currentMap = {}
  contentMap['name'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2011-08-05-11:53:29_00001'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.name'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.name'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2011-08-05-11:53:29_00001'
  currentMap['name'] = 'name'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute MolSystemSymmetrySet.symmetrySetId
  currentMap = {}
  contentMap['symmetrySetId'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00009'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.symmetrySetId'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.symmetrySetId'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00009'
  currentMap['name'] = 'symmetrySetId'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00001')

  # Role MolSystemSymmetrySet.access
  contentMap['access'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:03:01_00014')

  # Role MolSystemSymmetrySet.molSystem
  currentMap = {}
  contentMap['molSystem'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00006'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.molSystem'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.molSystem'
  currentMap['type'] = 'exotop'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00006'
  currentMap['name'] = 'molSystem'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['copyOverride'] = True
  currentMap['content'] = globalMap.get('MOLS').get('exolinks')

  # Role MolSystemSymmetrySet.symmetries
  currentMap = {}
  contentMap['symmetries'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00008'] = currentMap
  loadMaps['SYMM.MolSystemSymmetrySet.symmetries'] = currentMap
  currentMap['tag'] = 'SYMM.MolSystemSymmetrySet.symmetries'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00008'
  currentMap['name'] = 'symmetries'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['implSkip'] = True
  currentMap['content'] = globalMap.get('SYMM').get('abstractTypes')
  # End of MolSystemSymmetrySet

  currentMap = abstractTypes.get('MolSystemSymmetrySet')
  aList = ['createdBy', 'guid', 'isModifiable', 'lastUnlockedBy', 'symmetrySetId']
  currentMap['headerAttrs'] = aList
  aList = ['details', 'name']
  currentMap['simpleAttrs'] = aList
  aList = ['symmetries', 'molSystem', 'access', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['symmetries']
  currentMap['children'] = aList

  # Class Segment
  currentMap = {}
  abstractTypes['Segment'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00004'] = currentMap
  loadMaps['SYMM.Segment'] = currentMap
  currentMap['tag'] = 'SYMM.Segment'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00004'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'segments'
  currentMap['class'] = molsim.api.Symmetry.Segment
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Segment.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Segment.chainCode
  currentMap = {}
  contentMap['chainCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00010'] = currentMap
  loadMaps['SYMM.Segment.chainCode'] = currentMap
  currentMap['tag'] = 'SYMM.Segment.chainCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00010'
  currentMap['name'] = 'chainCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['eType'] = 'cplx'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033')

  # Attribute Segment.firstSeqId
  currentMap = {}
  contentMap['firstSeqId'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00011'] = currentMap
  loadMaps['SYMM.Segment.firstSeqId'] = currentMap
  currentMap['tag'] = 'SYMM.Segment.firstSeqId'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:58_00011'
  currentMap['name'] = 'firstSeqId'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['proc'] = 'direct'
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Role Segment.access
  contentMap['access'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:03:01_00014')
  # End of Segment

  currentMap = abstractTypes.get('Segment')
  aList = ['firstSeqId']
  currentMap['headerAttrs'] = aList
  aList = ['chainCode']
  currentMap['simpleAttrs'] = aList
  aList = ['access', 'applicationData']
  currentMap['cplxAttrs'] = aList

  # Class Symmetry
  currentMap = {}
  abstractTypes['Symmetry'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00002'] = currentMap
  loadMaps['SYMM.Symmetry'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry'
  currentMap['type'] = 'class'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00002'
  currentMap['eType'] = 'cplx'
  currentMap['fromParent'] = 'symmetries'
  currentMap['objkey'] = 'serial'
  currentMap['class'] = molsim.api.Symmetry.Symmetry
  contentMap = {}
  currentMap['content'] = contentMap

  # Attribute Symmetry.applicationData
  contentMap['applicationData'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-09-14-18:48:27_00007')

  # Attribute Symmetry.segmentLength
  currentMap = {}
  contentMap['segmentLength'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00004'] = currentMap
  loadMaps['SYMM.Symmetry.segmentLength'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry.segmentLength'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00004'
  currentMap['name'] = 'segmentLength'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:54_00001')

  # Attribute Symmetry.serial
  currentMap = {}
  contentMap['serial'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00002'] = currentMap
  loadMaps['SYMM.Symmetry.serial'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry.serial'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00002'
  currentMap['name'] = 'serial'
  currentMap['hicard'] = 1
  currentMap['locard'] = 1
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032')

  # Attribute Symmetry.symmetryCode
  currentMap = {}
  contentMap['symmetryCode'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00003'] = currentMap
  loadMaps['SYMM.Symmetry.symmetryCode'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry.symmetryCode'
  currentMap['type'] = 'attr'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00003'
  currentMap['name'] = 'symmetryCode'
  currentMap['hicard'] = 1
  currentMap['locard'] = 0
  currentMap['data'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00006')

  # Role Symmetry.access
  contentMap['access'] = mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-12-31-09:03:01_00014')

  # Role Symmetry.segments
  currentMap = {}
  contentMap['segments'] = currentMap
  mapsByGuid['www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00001'] = currentMap
  loadMaps['SYMM.Symmetry.segments'] = currentMap
  currentMap['tag'] = 'SYMM.Symmetry.segments'
  currentMap['type'] = 'child'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:59_00001'
  currentMap['name'] = 'segments'
  currentMap['hicard'] = -1
  currentMap['locard'] = 0
  currentMap['eType'] = 'cplx'
  currentMap['content'] = globalMap.get('SYMM').get('abstractTypes')
  # End of Symmetry

  currentMap = abstractTypes.get('Symmetry')
  aList = ['segmentLength', 'serial', 'symmetryCode']
  currentMap['headerAttrs'] = aList
  aList = ['segments', 'access', 'applicationData']
  currentMap['cplxAttrs'] = aList
  aList = ['segments']
  currentMap['children'] = aList

  # Out-of-package link to MolSystemSymmetrySet
  currentMap = {}
  exolinks['MolSystemSymmetrySet'] = currentMap
  loadMaps['SYMM.exo-MolSystemSymmetrySet'] = currentMap
  currentMap['tag'] = 'SYMM.exo-MolSystemSymmetrySet'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00001'
  currentMap['name'] = 'MolSystemSymmetrySet'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = molsim.api.Symmetry.MolSystemSymmetrySet
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))

  # Out-of-package link to Segment
  currentMap = {}
  exolinks['Segment'] = currentMap
  loadMaps['SYMM.exo-Segment'] = currentMap
  currentMap['tag'] = 'SYMM.exo-Segment'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00004'
  currentMap['name'] = 'Segment'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = molsim.api.Symmetry.Segment
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00033'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))

  # Out-of-package link to Symmetry
  currentMap = {}
  exolinks['Symmetry'] = currentMap
  loadMaps['SYMM.exo-Symmetry'] = currentMap
  currentMap['tag'] = 'SYMM.exo-Symmetry'
  currentMap['type'] = 'exo'
  currentMap['guid'] = 'www.ccpn.ac.uk_Fogh_2008-02-20-18:17:09_00002'
  currentMap['name'] = 'Symmetry'
  currentMap['eType'] = 'cplx'
  currentMap['class'] = molsim.api.Symmetry.Symmetry
  aList = list()
  currentMap['keyMaps'] = aList
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2008-06-30-16:30:50_00001'))
  aList.append(mapsByGuid.get('www.ccpn.ac.uk_Fogh_2006-08-16-14:22:53_00032'))