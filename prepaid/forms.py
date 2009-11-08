from django import forms

class WithdrawalForm(forms.Form):
	amount = forms.IntegerField(help_text='Number of points to withdraw')
	paypal_email = forms.EmailField(help_text='Paypal email to send money to')
