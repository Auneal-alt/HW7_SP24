from PyQt5 import QtCore, QtGui, QtWidgets


class Ui__frm_StateCalculator(object):
    def setupUi(self, _frm_StateCalculator):
        _frm_StateCalculator.setObjectName("_frm_StateCalculator")
        _frm_StateCalculator.resize(528, 516)
        self.verticalLayout = QtWidgets.QVBoxLayout(_frm_StateCalculator)
        self.verticalLayout.setObjectName("verticalLayout")

        # Group box for System of Units
        self._grp_Units = QtWidgets.QGroupBox(_frm_StateCalculator)
        self._grp_Units.setObjectName("_grp_Units")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self._grp_Units)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._rdo_SI = QtWidgets.QRadioButton(self._grp_Units)
        self._rdo_SI.setChecked(True)
        self._rdo_SI.setObjectName("_rdo_SI")
        self.horizontalLayout_2.addWidget(self._rdo_SI)
        self._rdo_English = QtWidgets.QRadioButton(self._grp_Units)
        self._rdo_English.setObjectName("_rdo_English")
        self.horizontalLayout_2.addWidget(self._rdo_English)
        self.verticalLayout.addWidget(self._grp_Units)

        # Group box for Specified Properties
        self._grp_SpecifiedProperties = QtWidgets.QGroupBox(_frm_StateCalculator)
        self._grp_SpecifiedProperties.setObjectName("_grp_SpecifiedProperties")
        self.gridLayout = QtWidgets.QGridLayout(self._grp_SpecifiedProperties)
        self.gridLayout.setObjectName("gridLayout")

        # Group box for State 1
        self._grp_State1 = QtWidgets.QGroupBox(self._grp_SpecifiedProperties)
        self._grp_State1.setObjectName("_grp_State1")
        self.gridLayout_State1 = QtWidgets.QGridLayout(self._grp_State1)
        self.gridLayout_State1.setObjectName("gridLayout_State1")
        self.gridLayout.addWidget(self._grp_State1, 0, 0, 1, 1)

        # Group box for State 2
        self._grp_State2 = QtWidgets.QGroupBox(self._grp_SpecifiedProperties)
        self._grp_State2.setObjectName("_grp_State2")
        self.gridLayout_State2 = QtWidgets.QGridLayout(self._grp_State2)
        self.gridLayout_State2.setObjectName("gridLayout_State2")
        self.gridLayout.addWidget(self._grp_State2, 0, 1, 1, 1)

        # Labels and input fields for State 1 properties
        self._le_State1_Property1 = QtWidgets.QLineEdit(self._grp_State1)
        self._le_State1_Property1.setObjectName("_le_State1_Property1")
        self.gridLayout_State1.addWidget(self._le_State1_Property1, 0, 0, 1, 1)
        # Add more labels and input fields as needed for State 1 properties

        # Labels and input fields for State 2 properties
        self._le_State2_Property1 = QtWidgets.QLineEdit(self._grp_State2)
        self._le_State2_Property1.setObjectName("_le_State2_Property1")
        self.gridLayout_State2.addWidget(self._le_State2_Property1, 0, 0, 1, 1)
        # Add more labels and input fields as needed for State 2 properties

        self.verticalLayout.addWidget(self._grp_SpecifiedProperties)

        # Group box for State Properties
        self._grp_StateProperties = QtWidgets.QGroupBox(_frm_StateCalculator)
        self._grp_StateProperties.setObjectName("_grp_StateProperties")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._grp_StateProperties)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Group box for State 1 properties in State Properties
        self._grp_State1_Properties = QtWidgets.QGroupBox(self._grp_StateProperties)
        self._grp_State1_Properties.setObjectName("_grp_State1_Properties")
        self.horizontalLayout_State1 = QtWidgets.QHBoxLayout(self._grp_State1_Properties)
        self.horizontalLayout_State1.setObjectName("horizontalLayout_State1")
        self.verticalLayout_2.addWidget(self._grp_State1_Properties)

        # Group box for State 2 properties in State Properties
        self._grp_State2_Properties = QtWidgets.QGroupBox(self._grp_StateProperties)
        self._grp_State2_Properties.setObjectName("_grp_State2_Properties")
        self.horizontalLayout_State2 = QtWidgets.QHBoxLayout(self._grp_State2_Properties)
        self.horizontalLayout_State2.setObjectName("horizontalLayout_State2")
        self.verticalLayout_2.addWidget(self._grp_State2_Properties)

        # Group box for State Change properties in State Properties
        self._grp_StateChange_Properties = QtWidgets.QGroupBox(self._grp_StateProperties)
        self._grp_StateChange_Properties.setObjectName("_grp_StateChange_Properties")
        self.horizontalLayout_StateChange = QtWidgets.QHBoxLayout(self._grp_StateChange_Properties)
        self.horizontalLayout_StateChange.setObjectName("horizontalLayout_StateChange")
        self.verticalLayout_2.addWidget(self._grp_StateChange_Properties)

        self.verticalLayout.addWidget(self._grp_StateProperties)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(_frm_StateCalculator)
        self._cmb_Property2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(_frm_StateCalculator)

    def retranslateUi(self, _frm_StateCalculator):
        _translate = QtCore.QCoreApplication.translate
        _frm_StateCalculator.setWindowTitle(_translate("_frm_StateCalculator", "Thermodynamic State Calculator"))
        self._grp_Units.setTitle(_translate("_frm_StateCalculator", "System of Units"))
        self._rdo_SI.setText(_translate("_frm_StateCalculator", "SI"))
        self._rdo_English.setText(_translate("_frm_StateCalculator", "English"))
        self._grp_SpecifiedProperties.setTitle(_translate("_frm_StateCalculator", "Specified Properties"))
        # Add labels and texts for State 1 and State 2 properties
        self._grp_State1.setTitle(_translate("_frm_StateCalculator", "State 1"))
        self._grp_State2.setTitle(_translate("_frm_StateCalculator", "State 2"))
        # Add labels for State Properties group boxes
        self._grp_State1_Properties.setTitle(_translate("_frm_StateCalculator", "State 1 Properties"))
        self._grp_State2_Properties.setTitle(_translate("_frm_StateCalculator", "State 2 Properties"))
        self._grp_StateChange_Properties.setTitle(_translate("_frm_StateCalculator", "State Change Properties"))
