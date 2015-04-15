# -------------------- Import Statements --------------------
from __future__ import division
import os
from sys import exit
import random

from general_functions import *

# -----------------------------------------------------------
# ------------ Character Base Classes/Subclasses ------------		
class Character(object):
	
	def __init__(self):
		# Combat related attributes
		self.max_health = 100
		self.current_health = 100
		
	def do_damage_controlled(self, enemy):
		# Checks whether someone has been dropped to zero health
		if enemy.current_health > 0 and self.current_health > 0:
			if random.uniform(20, (self.attack_rating_modified + (self.agility_rating_modified/2))) < (enemy.agility_rating_modified/2):
				self.damage = 0
			else:
				self.damage = random.uniform(10,15 + (self.strength_rating_modified/10))
				self.damage_after_mitigation = (self.damage - (enemy.defense_rating_modified/10))
				# This prevents the damage done from being higher than the current health of enemy.
				if self.damage_after_mitigation > enemy.current_health:
					self.damage_after_mitigation = enemy.current_health
				else:
					self.damage_after_mitigation = self.damage_after_mitigation
			# Checks whether enemy is fast enough to evade your attack
			if self.damage == 0:
				enemy.current_health = enemy.current_health
				print "%s evades %s's attack!" % (enemy.name, self.name)
				print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to prevent damage 
			elif self.damage <= (enemy.defense_rating_modified/10) and (enemy.defense_rating_modified/10) > 0:
				enemy.current_health = enemy.current_health
				print "%s's defense rating of %0.2f prevents damage from %s." % (enemy.name, enemy.defense_rating_modified, self.name)
				print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to mitigate some of the damage
			elif self.damage > (enemy.defense_rating_modified/10) and (enemy.defense_rating_modified/10) > 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'out of combat'
					print "%s's defense rating of %0.2f mitigates %0.2f damage from %s, " % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified/10, self.name)
					print "only allowing %0.2f damage through." % self.damage_after_mitigation
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						print "%s has been eliminated!" % enemy.name
						enemy.loot_drop()
						self.level_check()
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.strength_rating_modified = self.strength_rating
						self.defense_rating_modified = self.defense_rating
						self.magic_rating_modified = self.magic_rating
						self.agility_rating_modified = self.agility_rating
						# This adds the enemy to the enemies_killed list to assist with load_enemy.
						self.enemies_killed.append(enemy.name)
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "%s has been eliminated!" % me.name
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s's defense rating of %0.2f mitigates %0.2f damage from %s, " % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified/10, self.name)
					print "only allowing %0.2f damage through." % self.damage_after_mitigation
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether the enemy is hit directly with your attack
			elif self.damage_after_mitigation > 0 and (enemy.defense_rating_modified/10) == 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'out of combat'
					print "%s suffers %0.2f damage from %s's attack!" % (enemy.name, self.damage_after_mitigation, self.name)
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						print "%s has been eliminated!" % enemy.name
						enemy.loot_drop()
						self.level_check()
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.strength_rating_modified = self.strength_rating
						self.defense_rating_modified = self.defense_rating
						self.magic_rating_modified = self.magic_rating
						self.agility_rating_modified = self.agility_rating
						# This adds the enemy to the enemies_killed list to assist with load_enemy.
						self.enemies_killed.append(enemy.name)
					# Otherwise, the player (who is without a 'drop_table') must have died.
					else:
						print "%s has been eliminated!" % me.name
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still is alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s suffers %0.2f damage from %s's attack!" % (enemy.name, self.damage_after_mitigation, self.name)
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)	
		
	def do_damage_balanced(self, enemy):
		# Checks whether someone has been dropped to zero health
		if enemy.current_health > 0 and self.current_health > 0:
			if random.uniform(10, (self.attack_rating_modified + (self.agility_rating_modified/2))) < (enemy.agility_rating_modified/2):
				self.damage = 0
			else:
				self.damage = random.uniform(5,20 + (self.strength_rating_modified/10))
				self.damage_after_mitigation = (self.damage - (enemy.defense_rating_modified/10))
				# This prevents the damage done from being higher than the current health of enemy.
				if self.damage_after_mitigation > enemy.current_health:
					self.damage_after_mitigation = enemy.current_health
				else:
					self.damage_after_mitigation = self.damage_after_mitigation
			# Checks whether enemy is fast enough to evade your attack
			if self.damage == 0:
				enemy.current_health = enemy.current_health
				print "%s evades %s's attack!" % (enemy.name, self.name)
				print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to prevent damage 
			elif self.damage <= (enemy.defense_rating_modified/10) and (enemy.defense_rating_modified/10) > 0:
				enemy.current_health = enemy.current_health
				print "%s's defense rating of %0.2f prevents damage from %s." % (enemy.name, enemy.defense_rating_modified, self.name)
				print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to mitigate some of the damage
			elif self.damage > (enemy.defense_rating_modified/10) and (enemy.defense_rating_modified/10) > 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'out of combat'
					print "%s's defense rating of %0.2f mitigates %0.2f damage from %s, " % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified/10, self.name)
					print "only allowing %0.2f damage through." % self.damage_after_mitigation
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						print "%s has been eliminated!" % enemy.name
						enemy.loot_drop()
						self.level_check()
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.strength_rating_modified = self.strength_rating
						self.defense_rating_modified = self.defense_rating
						self.magic_rating_modified = self.magic_rating
						self.agility_rating_modified = self.agility_rating
						# This adds the enemy to the enemies_killed list to assist with load_enemy.
						self.enemies_killed.append(enemy.name)
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "%s has been eliminated!" % me.name
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s's defense rating of %0.2f mitigates %0.2f damage from %s, " % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified/10, self.name)
					print "only allowing %0.2f damage through." % self.damage_after_mitigation
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether the enemy is hit directly with your attack
			elif self.damage_after_mitigation > 0 and (enemy.defense_rating_modified/10) == 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'out of combat'
					print "%s suffers %0.2f damage from %s's attack!" % (enemy.name, self.damage_after_mitigation, self.name)
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						print "%s has been eliminated!" % enemy.name
						enemy.loot_drop()
						self.level_check()
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.strength_rating_modified = self.strength_rating
						self.defense_rating_modified = self.defense_rating
						self.magic_rating_modified = self.magic_rating
						self.agility_rating_modified = self.agility_rating
						# This adds the enemy to the enemies_killed list to assist with load_enemy.
						self.enemies_killed.append(enemy.name)
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "%s has been eliminated!" % me.name
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still is alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s suffers %0.2f damage from %s's attack!" % (enemy.name, self.damage_after_mitigation, self.name)
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
	
	def do_damage_aggressive(self, enemy):
		# Checks whether someone has been dropped to zero health
		if enemy.current_health > 0 and self.current_health > 0:
			if random.uniform(0, (self.attack_rating_modified + (self.agility_rating_modified/2))) < (enemy.agility_rating_modified/2):
				self.damage = 0
			else:
				self.damage = random.uniform(5,25 + (self.strength_rating_modified/10))
				self.damage_after_mitigation = (self.damage - (enemy.defense_rating_modified/10))
				# This prevents the damage done from being higher than the current health of enemy.
				if self.damage_after_mitigation > enemy.current_health:
					self.damage_after_mitigation = enemy.current_health
				else:
					self.damage_after_mitigation = self.damage_after_mitigation
			# Checks whether enemy is fast enough to evade your attack
			if self.damage == 0:
				enemy.current_health = enemy.current_health
				print "%s evades %s's attack!" % (enemy.name, self.name)
				print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to prevent damage 
			elif self.damage <= (enemy.defense_rating_modified/10) and (enemy.defense_rating_modified/10) > 0:
				enemy.current_health = enemy.current_health
				print "%s's defense rating of %0.2f prevents damage from %s." % (enemy.name, enemy.defense_rating_modified, self.name)
				print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to mitigate some of the damage
			elif self.damage > (enemy.defense_rating_modified/10) and (enemy.defense_rating_modified/10) > 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'out of combat'
					print "%s's defense rating of %0.2f mitigates %0.2f damage from %s, " % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified/10, self.name)
					print "only allowing %0.2f damage through." % self.damage_after_mitigation
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						print "%s has been eliminated!" % enemy.name
						enemy.loot_drop()
						self.level_check()
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.strength_rating_modified = self.strength_rating
						self.defense_rating_modified = self.defense_rating
						self.magic_rating_modified = self.magic_rating
						self.agility_rating_modified = self.agility_rating
						# This adds the enemy to the enemies_killed list to assist with load_enemy.
						self.enemies_killed.append(enemy.name)
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "%s has been eliminated!" % me.name
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s's defense rating of %0.2f mitigates %0.2f damage from %s, " % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified/10, self.name)
					print "only allowing %0.2f damage through." % self.damage_after_mitigation
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
			# Checks whether the enemy is hit directly with your attack
			elif self.damage_after_mitigation > 0 and (enemy.defense_rating_modified/10) == 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'out of combat'
					print "%s suffers %0.2f damage from %s's attack!" % (enemy.name, self.damage_after_mitigation, self.name)
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						print "%s has been eliminated!" % enemy.name
						enemy.loot_drop()
						self.level_check()
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.strength_rating_modified = self.strength_rating
						self.defense_rating_modified = self.defense_rating
						self.magic_rating_modified = self.magic_rating
						self.agility_rating_modified = self.agility_rating
						# This adds the enemy to the enemies_killed list to assist with load_enemy.
						self.enemies_killed.append(enemy.name)
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "%s has been eliminated!" % me.name
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still is alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s suffers %0.2f damage from %s's attack!" % (enemy.name, self.damage_after_mitigation, self.name)
					print "%s has %0.2f health remaining." % (enemy.name, enemy.current_health)
	
	
# --------------- Character Subclass Enemy ------------------
class Enemy(Character):

	def __init__(self):
		Character.__init__(self)
		# These are the original combat attributes.
		self.max_health = 100
		self.current_health = 100
		self.attack_rating = 0
		self.strength_rating = 0
		self.defense_rating = 0
		self.agility_rating = 0
		# These are needed to preserve original combat attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
				
	def loot_drop(self):
		self.gold_dropped = self.gold
		self.experience_rewarded = self.experience
		me.experience += self.experience_rewarded
		Player.inventory['gold'] += self.gold_dropped
		self.loot_dropped = random.choice(self.drop_table['potions'])
		if self.loot_dropped in Player.inventory['potions']:
			Player.inventory['potions'][self.loot_dropped] += 1
		elif self.loot_dropped not in Player.inventory['potions']:
			Player.inventory['potions'][self.loot_dropped] = 1
			
		# Checks whether the loot dropped begins with vowel
		if vowel_check(self.loot_dropped) == True:
			print "\nYou gain %0.2f experience." % self.experience_rewarded
			print "An %s and %d gold are added to your inventory!" % (self.loot_dropped, self.gold_dropped)
		else:
			print "\nYou gain %0.2f experience." % self.experience_rewarded
			print "A %s and %d gold are added to your inventory!" % (self.loot_dropped, self.gold_dropped)

# -------------------- Enemy Subclasses ---------------------
class GiantScorpion(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Giant Scorpion'
		# These are the original combat attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 55
		self.strength_rating = 20
		self.defense_rating = 30
		self.magic_rating = 0
		self.agility_rating = 30
		self.alignment = "Neutral"
		# These are needed to preserve original combat attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_controlled
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'defense potion'],
			}
			

class Ghoul(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Ghoul'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 40
		self.strength_rating = 25
		self.defense_rating = 25
		self.magic_rating = 0
		self.agility_rating = 40
		self.alignment = "Dark"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'attack potion'],
			}


class Satyr(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Satyr'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 45
		self.strength_rating = 30
		self.defense_rating = 20
		self.magic_rating = 0
		self.agility_rating = 45
		self.alignment = "Dark"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'agility potion'],
			}			
			
			
class Knight(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Knight'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 50
		self.strength_rating = 50
		self.defense_rating = 50
		self.magic_rating = 0
		self.agility_rating = 35
		self.alignment = "Light"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_balanced
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'defense potion'],
			}
			

class Ogre(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Ogre'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 30
		self.strength_rating = 65
		self.defense_rating = 40
		self.magic_rating = 0
		self.agility_rating = 25
		self.alignment = "Dark"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'strength potion'],
			}
			

class Gargoyle(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Gargoyle'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 45
		self.strength_rating = 45
		self.defense_rating = 45
		self.magic_rating = 0
		self.agility_rating = 60
		self.alignment = "Light"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_balanced
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'defense potion'],
			}
			

class Gryphon(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Gryphon'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 35
		self.strength_rating = 35
		self.defense_rating = 40
		self.magic_rating = 0
		self.agility_rating = 85
		self.alignment = "Light"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_controlled
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'agility potion'],
			}
			

class Harpy(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Harpy'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 60
		self.strength_rating = 25
		self.defense_rating = 30
		self.magic_rating = 0
		self.agility_rating = 55
		self.alignment = "Dark"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_controlled
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'agility potion'],
			}
			

class Centaur(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Centaur'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 50
		self.strength_rating = 60
		self.defense_rating = 40
		self.magic_rating = 0
		self.agility_rating = 50
		self.alignment = "Neutral"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_balanced
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'attack potion'],
			}
			

class Cyclops(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Cyclops'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 45
		self.strength_rating = 80
		self.defense_rating = 60
		self.magic_rating = 0
		self.agility_rating = 25
		self.alignment = "Neutral"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'strength potion'],
			}
			
			
class Werewolf(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Werewolf'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 45
		self.strength_rating = 60
		self.defense_rating = 40
		self.magic_rating = 0
		self.agility_rating = 50
		self.alignment = "Dark"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'agility potion'],
			}
			

class Chimera(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Chimera'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 55
		self.strength_rating = 55
		self.defense_rating = 35
		self.magic_rating = 0
		self.agility_rating = 65
		self.alignment = "Dark"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'strength potion'],
			}


class Dragon(Enemy):
	
	def __init__(self):
		Character.__init__(self)
		self.name = 'Dragon'
		# These are the original attributes.
		self.max_health = 100
		self.current_health = 100
		self.max_mana = 0
		self.current_mana = 0
		self.attack_rating = 65
		self.strength_rating = 65
		self.defense_rating = 65
		self.magic_rating = 0
		self.agility_rating = 55
		self.alignment = "Neutral"
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# These are the rewards for slaying this enemy.
		self.experience = (self.attack_rating + self.strength_rating + self.defense_rating + self.magic_rating + self.agility_rating)
		self.gold = (self.experience/10)
		self.drop_table = {
			'potions': ['health potion', 'attack potion'],
			}
		
			
# --------------- Character Subclass Player -----------------			
class Player(Character):

	inventory = {
		'gold': 0,
		'potions': {'health potion': 2, 'mana potion': 2},
	}
	
	light_spell_book = {
		'New Light': 5,
		'Hard Light': 10,
		'Nearmost Light': 15,
		'Farmost Light': 15,
		'Inmost Light': 20,
	}
	
	dark_spell_book = {
		'New Dark': 5,
		'Shadow Walk': 10,
		'Light Drain': 20,
		'From Beyond The Shadows': 15,
		'Corruption': 20,
	}
	
	def __init__(self):
		Character.__init__(self)
		self.state = 'out of combat'
		self.total_attribute_points = 250
		self.alignment = ""
		# These are needed for the leveling system.
		self.experience = 0
		self.combat_level = 1
		# These are the original attributes.
		self.max_mana = 100
		self.current_mana = 100
		self.attack_rating = 0
		self.strength_rating = 0
		self.defense_rating = 0
		self.magic_rating = 0
		self.agility_rating = 0
		# These are needed to preserve original attribute values between fights.
		self.attack_rating_modified = self.attack_rating
		self.strength_rating_modified = self.strength_rating
		self.defense_rating_modified = self.defense_rating
		self.magic_rating_modified = self.magic_rating
		self.agility_rating_modified = self.agility_rating
		# This list of enemies killed is needed to help with load_enemy.
		self.enemies_killed = []
		
	def quit(self):
		are_you_sure = raw_input("Are you sure you want to leave the combat simulator? (Yes/No) ")
		if are_you_sure.upper() == 'YES':
			print "You log out of the combat simulator."
			os.system('pause')
			exit(0)
		elif are_you_sure.upper() == 'NO':
			print "You change your mind and continue on with your training."
		else:
			print "You entered %s when you should have entered Yes or No." % are_you_sure
	
	def help(self):
		print "To access any of the player commands simply type any of the following:\n"
		print 'quit 		| Leaves the combat simulator'
		print 'help 		| Displays available commands'
		print 'load scores	| Displays information on past participants'
		print 'load enemy 	| Loads the next enemy into the combat simulator'
		print 'inventory 	| Displays user inventory'
		print 'use potion 	| Prompts user to enter a potion to drink'
		print 'enemy status	| Displays enemy status'
		print 'status 		| Displays user status'
		print 'show stances	| Displays attack stances that are avaiable for melee' 
		print 'show spells 	| Displays spells that are available'
		print 'melee attack	| Prompts user to enter melee style to use'
		print 'cast spell 	| Prompts user to enter spell to cast'
		
	def status(self):
		print "---------------------"
		print "Combat level: %d" % self.combat_level
		print "Health: %0.2f/%0.2f" % (me.current_health, me.max_health)
		print "Mana: %0.2f/%0.2f" % (me.current_mana, me.max_mana)
		print "State: %s" % me.state
		print "Attack rating: %0.2f" % me.attack_rating_modified
		print "Strength rating: %0.2f" % me.strength_rating_modified
		print "Defense rating: %0.2f" % me.defense_rating_modified
		print "Magic rating: %0.2f" % me.magic_rating_modified
		print "Agility rating: %0.2f" % me.agility_rating_modified
		print "Experience: %0.2f" % self.experience
		print "---------------------"
		
	def enemy_status(self):
		print "---------------------"
		print "Alignment: %s" % me.enemy.alignment
		print "Health: %0.2f/%0.2f" % (me.enemy.current_health, me.enemy.max_health)
		print "Mana: %0.2f/%0.2f" % (me.enemy.current_mana, me.enemy.max_mana)
		print "Attack rating: %0.2f" % me.enemy.attack_rating_modified
		print "Strength rating: %0.2f" % me.enemy.strength_rating_modified
		print "Defense rating: %0.2f" % me.enemy.defense_rating_modified
		print "Magic rating: %0.2f" % me.enemy.magic_rating_modified
		print "Agility rating: %0.2f" % me.enemy.agility_rating_modified
		print "---------------------"
	
	def load_enemy(self):
		if self.state != 'out of combat':
			print "You must defeat the enemy that is already loaded before loading more."
		else:
			self.state = 'in combat'
			enemy = random.choice(EnemyDatabase.keys())
			if len(me.enemies_killed) == 12:
				print "Congratulations! You have survived the combat simulator."
				save_to_scores()
				os.system('pause')
				exit(0)
			elif me.enemies_killed.count(EnemyDatabase[enemy].name) == 0:
				enemy_instance = EnemyDatabase[enemy]
				me.enemy = enemy_instance
			elif me.enemies_killed.count(EnemyDatabase[enemy].name) != 0:
				enemy = random.choice(EnemyDatabase.keys())
				enemy_instance = EnemyDatabase[enemy]
				me.enemy = enemy_instance
					
			if vowel_check(enemy) == True:
				print "An %s is loaded into the simulation. Good luck!" % enemy
				return me.enemy
			else:
				print "A %s is loaded into the simulation. Good luck!" % enemy
				return me.enemy
						
	def show_inventory(self):
		print self.inventory		
		
	def use_potion(self, potion_used):
		self.potion_used = potion_used
		if self.potion_used in self.inventory['potions']:
			if self.inventory['potions'][self.potion_used] > 0:
				self.inventory['potions'][self.potion_used] -= 1
				if self.potion_used == 'health potion':
					if self.current_health + (self.max_health / 4) > self.max_health:
						self.health_gained = self.max_health - self.current_health
						self.current_health = self.max_health
						print "You gained %0.2f health from drinking the health potion." % self.health_gained
					else:
						self.current_health += (self.max_health / 4)
						self.health_gained = (self.max_health / 4)
						print "You gain %0.2f health from drinking the health potion." % self.health_gained
				elif self.potion_used == 'mana potion':
					if self.current_mana + (self.max_mana / 4) > self.max_mana:
						self.mana_gained = self.max_mana - self.current_mana
						self.current_mana = self.max_mana
						print "You gained %0.2f mana from drinking the mana potion." % self.mana_gained
					else:
						self.current_mana += (self.max_mana / 4)
						self.mana_gained = (self.max_mana / 4)
						print "You gain %0.2f mana from drinking the mana potion." % self.mana_gained
				elif self.potion_used == 'attack potion':
					self.attack_rating_modified += 5
					print "You gain 5 attack rating from drinking the attack potion."
				elif self.potion_used == 'strength potion':
					self.strength_rating_modified += 5
					print "You gain 5 strength rating from drinking the strength potion."
				elif self.potion_used == 'defense potion':
					self.defense_rating_modified += 5
					print "You gain 5 defense rating from drinking the defense potion."
				elif self.potion_used == 'agility potion':
					self.agility_rating_modified += 5
					print "You gain 5 agility rating from drinking the agility potion."
			else:
				print "You have none of that potion remaining."
		else:
			print "You don't have a potion with that name."
					
	def show_spells(self):
		if self.alignment == 'Light':
			if self.combat_level < 3:
				print "New Light: Low damage, increases defense rating of caster by 5%."
			elif self.combat_level < 5:
				print "New Light: Low damage, increases defense rating of caster by 5%."
				print "Hard Light: No damage, increases defense rating of caster by 20%."
			elif self.combat_level < 7:
				print "New Light: Low damage, increases defense rating of caster by 5%."
				print "Hard Light: No damage, increases defense rating of caster by 20%."
				print "Nearmost Light: Medium damage, increases defense rating of caster by 5%."
			elif self.combat_level < 9:
				print "New Light: Low damage, increases defense rating of caster by 5%."
				print "Hard Light: No damage, increases defense rating of caster by 20%."
				print "Nearmost Light: Medium damage, increases defense rating of caster by 5%."
				print "Farmost Light: High damage, no buffs or debuffs."
			else:
				print "New Light: Low damage, increases defense rating of caster by 5%."
				print "Hard Light: No damage, increases defense rating of caster by 20%."
				print "Nearmost Light: Medium damage, increases defense rating of caster by 5%."
				print "Farmost Light: High damage, no buffs or debuffs."
				print "Inmost Light: Medium damage, restores health of caster by 10% of max health."
		elif self.alignment == 'Dark':
			if self.combat_level < 3:
				print "New Dark: Low damage, decreases enemy defense rating by 5% during battle."
			elif self.combat_level < 5:
				print "New Dark: Low damage, decreases enemy defense by 5%."
				print "Shadow Walk: Low to medium damage, increases agility rating of caster by 20%."
			elif self.combat_level < 7:
				print "New Dark: Low damage, decreases enemy defense by 5%."
				print "Shadow Walk: Low to medium damage, increases agility rating of caster by 20%."
				print "Light Drain: No to high damage, restores mana of caster equal to damage dealt."
			elif self.combat_level < 9:
				print "New Dark: Low damage, decreases enemy defense by 5%."
				print "Shadow Walk: Low to medium damage, increases agility rating of caster by 20%."
				print "Light Drain: No to high damage, restores mana of caster equal to damage dealt."
				print "From Beyond The Shadows: Medium damage, unavoidable by enemy."
			else:
				print "New Dark: Low damage, decreases enemy defense by 5%."
				print "Shadow Walk: Low to medium damage, increases agility rating of caster by 20%."
				print "Light Drain: No to high damage, restores mana of caster equal to damage dealt."
				print "From Beyond The Shadows: Medium damage, unavoidable by enemy."
				print "Corruption: No to high damage, restores health of caster equal to damage dealt."
				
	def cast_spell(self):
		if self.state != 'in combat':
			print "You need to load an enemy before you can do that."
		else:
			spell_cast = raw_input("Which spell do you cast? ").title()
			print ""
			# These are the spells that can be cast if aligned with the light.
			if self.alignment == 'Light':
				# First Light Spell; already unlocked when you start the combat simulator
				if spell_cast == 'New Light' and self.current_mana - self.light_spell_book[spell_cast] >= 0:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = random.uniform(1,10 + (self.magic_rating_modified/10)) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = random.uniform(1,10 + (self.magic_rating_modified/10))
					elif self.alignment != self.enemy.alignment:
						spell_damage = random.uniform(1,10 + (self.magic_rating_modified/10)) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					spell_buff = 0.05
					self.current_mana -= self.light_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.light_spell_book[spell_cast])
					# This is the formula for determining if a spell hits or misses.
					if (self.enemy.agility_rating_modified/2) > random.uniform(0,(self.magic_rating_modified*2) + (self.agility_rating_modified/2)):
						print "%s misses %s." % (spell_cast, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
					else:
						# This is what happens if you have enough mana, don't miss, and kill the enemy.
						if self.enemy.current_health - spell_damage <= 0:
							self.enemy.current_health = 0
							self.state = 'out of combat'
							self.defense_rating_buffed = self.defense_rating_modified * spell_buff
							self.defense_rating_modified += self.defense_rating_buffed
							print "%s inflicts %0.2f damage on %s and boosts your defense rating by %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.defense_rating_buffed)
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							print "%s has been eliminated!" % self.enemy.name
							self.enemy.loot_drop()
							self.level_check()
							# This resets modified stats of user back to base after battle.
							self.attack_rating_modified = self.attack_rating
							self.strength_rating_modified = self.strength_rating
							self.defense_rating_modified = self.defense_rating
							self.magic_rating_modified = self.magic_rating
							self.agility_rating_modified = self.agility_rating
							# This adds the enemy to the enemies_killed list to assist with load_enemy.
							me.enemies_killed.append(self.enemy.name)
						# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
						else:
							self.defense_rating_buffed = self.defense_rating_modified * spell_buff
							self.defense_rating_modified += self.defense_rating_buffed
							print "%s inflicts %0.2f damage on %s and boosts your defense rating by %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.defense_rating_buffed)
							self.enemy.current_health -= spell_damage
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'New Light' and self.current_mana - self.light_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				# Second Light Spell; unlocked at level 3
				elif spell_cast == 'Hard Light' and self.current_mana - self.light_spell_book[spell_cast] >= 0 and self.combat_level >= 3:
					spell_damage = 0
					spell_buff = 0.20
					self.current_mana -= self.light_spell_book[spell_cast]
					self.defense_rating_buffed = self.defense_rating_modified * spell_buff
					self.defense_rating_modified += self.defense_rating_buffed
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.light_spell_book[spell_cast])
					print "%s boosts your defense rating by %0.2f." % (spell_cast, self.defense_rating_buffed)
					print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
					self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'Hard Light' and self.current_mana - self.light_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				# Third Light Spell; unlocked at level 5
				elif spell_cast == 'Nearmost Light' and self.current_mana - self.light_spell_book[spell_cast] >= 0 and self.combat_level >= 5:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10)) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10))
					elif self.alignment != self.enemy.alignment:
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10)) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					spell_buff = 0.05
					self.current_mana -= self.light_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.light_spell_book[spell_cast])
					# This is the formula for determining if a spell hits or misses.
					if (self.enemy.agility_rating_modified/2) > random.uniform(0,(self.magic_rating_modified*2) + (self.agility_rating_modified/2)):
						print "%s misses %s." % (spell_cast, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
					else:
						# This is what happens if you have enough mana, don't miss, and kill the enemy.
						if self.enemy.current_health - spell_damage <= 0:
							self.enemy.current_health = 0
							self.state = 'out of combat'
							self.defense_rating_buffed = self.defense_rating_modified * spell_buff
							self.defense_rating_modified += self.defense_rating_buffed
							print "%s inflicts %0.2f damage on %s and boosts your defense rating by %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.defense_rating_buffed)
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							print "%s has been eliminated!" % self.enemy.name
							self.enemy.loot_drop()
							self.level_check()
							# This resets modified stats of user back to base after battle.
							self.attack_rating_modified = self.attack_rating
							self.strength_rating_modified = self.strength_rating
							self.defense_rating_modified = self.defense_rating
							self.magic_rating_modified = self.magic_rating
							self.agility_rating_modified = self.agility_rating
							# This adds the enemy to the enemies_killed list to assist with load_enemy.
							me.enemies_killed.append(self.enemy.name)
						# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
						else:
							self.defense_rating_buffed = self.defense_rating_modified * spell_buff
							self.defense_rating_modified += self.defense_rating_buffed
							print "%s inflicts %0.2f damage on %s and boosts your defense rating by %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.defense_rating_buffed)
							self.enemy.current_health -= spell_damage
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'Nearmost Light' and self.current_mana - self.light_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				# Fourth Light Spell; unlocked at level 7
				elif spell_cast == 'Farmost Light' and self.current_mana - self.light_spell_book[spell_cast] >= 0 and self.combat_level >= 7:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = 20 + (self.magic_rating_modified/10) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = 20 + (self.magic_rating_modified/10)
					elif self.alignment != self.enemy.alignment:
						spell_damage = 20 + (self.magic_rating_modified/10) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					self.current_mana -= self.light_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.light_spell_book[spell_cast])
					# This is the formula for determining if a spell hits or misses.
					if (self.enemy.agility_rating_modified/2) > random.uniform(0,(self.magic_rating_modified*2) + (self.agility_rating_modified/2)):
						print "%s misses %s." % (spell_cast, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
					else:
						# This is what happens if you have enough mana, don't miss, and kill the enemy.
						if self.enemy.current_health - spell_damage <= 0:
							self.enemy.current_health = 0
							self.state = 'out of combat'
							print "%s inflicts %0.2f damage on %s." % (spell_cast, spell_damage, self.enemy.name)
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							print "%s has been eliminated!" % self.enemy.name
							self.enemy.loot_drop()
							self.level_check()
							# This resets modified stats of user back to base after battle.
							self.attack_rating_modified = self.attack_rating
							self.strength_rating_modified = self.strength_rating
							self.defense_rating_modified = self.defense_rating
							self.magic_rating_modified = self.magic_rating
							self.agility_rating_modified = self.agility_rating
							# This adds the enemy to the enemies_killed list to assist with load_enemy.
							me.enemies_killed.append(self.enemy.name)
						# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
						else:
							print "%s inflicts %0.2f damage on %s." % (spell_cast, spell_damage, self.enemy.name)
							self.enemy.current_health -= spell_damage
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'Farmost Light' and self.current_mana - self.light_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				# Fifth Light Spell; unlocked at level 9
				elif spell_cast == 'Inmost Light' and self.current_mana - self.light_spell_book[spell_cast] >= 0 and self.combat_level >= 9:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10)) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10))
					elif self.alignment != self.enemy.alignment:
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10)) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					spell_buff = 0.10
					self.current_mana -= self.light_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.light_spell_book[spell_cast])
					# This is the formula for determining if a spell hits or misses.
					if (self.enemy.agility_rating_modified/2) > random.uniform(0,(self.magic_rating_modified*2) + (self.agility_rating_modified/2)):
						print "%s misses %s." % (spell_cast, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
					else:
						# This is what happens if you have enough mana, don't miss, and kill the enemy.
						if self.enemy.current_health - spell_damage <= 0:
							self.enemy.current_health = 0
							self.state = 'out of combat'
							if self.current_health + (self.max_health * spell_buff) > self.max_health:
								self.health_gained_from_spell = self.max_health - self.current_health
								self.current_health = self.max_health
							else:
								self.health_gained_from_spell = (self.max_health * spell_buff)
								self.current_health = self.current_health + self.health_gained_from_spell
							print "%s inflicts %0.2f damage on %s and heals you for %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.health_gained_from_spell)
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							print "%s has been eliminated!" % self.enemy.name
							self.enemy.loot_drop()
							self.level_check()
							# This resets modified stats of user back to base after battle.
							self.attack_rating_modified = self.attack_rating
							self.strength_rating_modified = self.strength_rating
							self.defense_rating_modified = self.defense_rating
							self.magic_rating_modified = self.magic_rating
							self.agility_rating_modified = self.agility_rating
							# This adds the enemy to the enemies_killed list to assist with load_enemy.
							me.enemies_killed.append(self.enemy.name)
						# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
						else:
							if self.current_health + (self.max_health * spell_buff) > self.max_health:
								self.health_gained_from_spell = self.max_health - self.current_health
								self.current_health = self.max_health
							else:
								self.health_gained_from_spell = (self.max_health * spell_buff)
								self.current_health = self.current_health + self.health_gained_from_spell 
							print "%s inflicts %0.2f damage on %s and heals you for %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.health_gained_from_spell)
							self.enemy.current_health -= spell_damage
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'Inmost Light' and self.current_mana - self.light_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				else:
					print "You don't have a spell with that name currently available."
			# These are spells that can be cast if aligned with the dark.
			elif self.alignment == 'Dark':
				# First Dark Spell; already unlocked when you start the combat simulator
				if spell_cast == 'New Dark' and self.current_mana - self.dark_spell_book[spell_cast] >= 0:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = random.uniform(1,10 + (self.magic_rating_modified/10)) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = random.uniform(1,10 + (self.magic_rating_modified/10))
					elif self.alignment != self.enemy.alignment:
						spell_damage = random.uniform(1,10 + (self.magic_rating_modified/10)) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					spell_debuff = 0.05
					self.current_mana -= self.dark_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.dark_spell_book[spell_cast])
					# This is the formula for determining if a spell hits or misses.
					if (self.enemy.agility_rating_modified/2) > random.uniform(0,(self.magic_rating_modified*2) + (self.agility_rating_modified/2)):
						print "%s misses %s." % (spell_cast, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
					else:
						# This is what happens if you have enough mana, don't miss, and kill the enemy.
						if self.enemy.current_health - spell_damage <= 0:
							self.enemy.current_health = 0
							self.state = 'out of combat'
							self.enemy.defense_rating_debuffed = self.enemy.defense_rating_modified * spell_debuff
							self.enemy.defense_rating_modified -= self.enemy.defense_rating_debuffed
							print "%s inflicts %0.2f damage on %s and lowers their defense rating by %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.enemy.defense_rating_debuffed)
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							print "%s has been eliminated!" % self.enemy.name
							self.enemy.loot_drop()
							self.level_check()
							# This resets modified stats of user back to base after battle.
							self.attack_rating_modified = self.attack_rating
							self.strength_rating_modified = self.strength_rating
							self.defense_rating_modified = self.defense_rating
							self.magic_rating_modified = self.magic_rating
							self.agility_rating_modified = self.agility_rating
							# This adds the enemy to the enemies_killed list to assist with load_enemy.
							me.enemies_killed.append(self.enemy.name)
						# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
						else:
							self.enemy.defense_rating_debuffed = self.enemy.defense_rating_modified * spell_debuff
							self.enemy.defense_rating_modified -= self.enemy.defense_rating_debuffed
							print "%s inflicts %0.2f damage on %s and lowers their defense rating by %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.enemy.defense_rating_debuffed)
							self.enemy.current_health -= spell_damage
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'New Dark' and self.current_mana - self.dark_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				# Second Dark Spell; unlocked at level 3
				elif spell_cast == 'Shadow Walk' and self.current_mana - self.dark_spell_book[spell_cast] >= 0 and self.combat_level >= 3:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = random.uniform(5,15 + (self.magic_rating_modified/10)) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = random.uniform(5,15 + (self.magic_rating_modified/10))
					elif self.alignment != self.enemy.alignment:
						spell_damage = random.uniform(5,15 + (self.magic_rating_modified/10)) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					spell_buff = 0.20
					self.current_mana -= self.dark_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.dark_spell_book[spell_cast])
					# This is the formula for determining if a spell hits or misses.
					if (self.enemy.agility_rating_modified/2) > random.uniform(0,(self.magic_rating_modified*2) + (self.agility_rating_modified/2)):
						print "%s misses %s." % (spell_cast, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
					else:
						# This is what happens if you have enough mana, don't miss, and kill the enemy.
						if self.enemy.current_health - spell_damage <= 0:
							self.enemy.current_health = 0
							self.state = 'out of combat'
							self.agility_rating_buffed = self.agility_rating_modified * spell_buff
							self.agility_rating_modified += self.agility_rating_buffed
							print "%s inflicts %0.2f damage on %s and boosts your agility rating by %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.agility_rating_buffed)
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							print "%s has been eliminated!" % self.enemy.name
							self.enemy.loot_drop()
							self.level_check()
							# This resets modified stats of user back to base after battle.
							self.attack_rating_modified = self.attack_rating
							self.strength_rating_modified = self.strength_rating
							self.defense_rating_modified = self.defense_rating
							self.magic_rating_modified = self.magic_rating
							self.agility_rating_modified = self.agility_rating
							# This adds the enemy to the enemies_killed list to assist with load_enemy.
							me.enemies_killed.append(self.enemy.name)
						# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
						else:
							self.agility_rating_buffed = self.agility_rating_modified * spell_buff
							self.agility_rating_modified += self.agility_rating_buffed
							print "%s inflicts %0.2f damage on %s and boosts your agility rating by %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.agility_rating_buffed)
							self.enemy.current_health -= spell_damage
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'Shadow Walk' and self.current_mana - self.dark_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				# Third Dark Spell; unlocked at level 5
				elif spell_cast == 'Light Drain' and self.current_mana - self.dark_spell_book[spell_cast] >= 0 and self.combat_level >= 5:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = random.uniform(0,20 + (self.magic_rating_modified/10)) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = random.uniform(0,20 + (self.magic_rating_modified/10))
					elif self.alignment != self.enemy.alignment:
						spell_damage = random.uniform(0,20 + (self.magic_rating_modified/10)) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					spell_buff = spell_damage
					self.current_mana -= self.dark_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.dark_spell_book[spell_cast])
					# This is the formula for determining if a spell hits or misses.
					if (self.enemy.agility_rating_modified/2) > random.uniform(0,(self.magic_rating_modified*2) + (self.agility_rating_modified/2)):
						print "%s misses %s." % (spell_cast, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
					else:
						# This is what happens if you have enough mana, don't miss, and kill the enemy.
						if self.enemy.current_health - spell_damage <= 0:
							self.enemy.current_health = 0
							self.state = 'out of combat'
							# This prevents user mana from being over their maximum mana.
							if self.current_mana + spell_buff > self.max_mana:
								self.current_mana = self.max_mana
							else:
								self.current_mana += spell_buff
							print "%s inflicts %0.2f damage on %s and restores %0.2f mana." % (spell_cast, spell_damage, self.enemy.name, spell_damage)
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							print "%s has been eliminated!" % self.enemy.name
							self.enemy.loot_drop()
							self.level_check()
							# This resets modified stats of user back to base after battle.
							self.attack_rating_modified = self.attack_rating
							self.strength_rating_modified = self.strength_rating
							self.defense_rating_modified = self.defense_rating
							self.magic_rating_modified = self.magic_rating
							self.agility_rating_modified = self.agility_rating
							# This adds the enemy to the enemies_killed list to assist with load_enemy.	
							me.enemies_killed.append(self.enemy.name)
						# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
						else:
							# This prevents user mana from being over their maximum mana.
							if self.current_mana + spell_buff > self.max_mana:
								self.current_mana = self.max_mana
							else:
								self.current_mana += spell_buff
							print "%s inflicts %0.2f damage on %s and restores %0.2f mana." % (spell_cast, spell_damage, self.enemy.name, spell_damage)
							self.enemy.current_health -= spell_damage
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'Light Drain' and self.current_mana - self.dark_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				# Fourth Dark Spell; unlocked at level 7
				elif spell_cast == 'From Beyond The Shadows' and self.current_mana - self.dark_spell_book[spell_cast] >= 0 and self.combat_level >= 7:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10)) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10))
					elif self.alignment != self.enemy.alignment:
						spell_damage = random.uniform(10,15 + (self.magic_rating_modified/10)) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					self.current_mana -= self.dark_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.dark_spell_book[spell_cast])
					# This is what happens if you have enough mana, don't miss, and kill the enemy.
					if self.enemy.current_health - spell_damage <= 0:
						self.enemy.current_health = 0
						self.state = 'out of combat'
						print "%s inflicts %0.2f damage on %s." % (spell_cast, spell_damage, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						print "%s has been eliminated!" % self.enemy.name
						self.enemy.loot_drop()
						self.level_check()
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.strength_rating_modified = self.strength_rating
						self.defense_rating_modified = self.defense_rating
						self.magic_rating_modified = self.magic_rating
						self.agility_rating_modified = self.agility_rating
						# This adds the enemy to the enemies_killed list to assist with load_enemy.
						me.enemies_killed.append(self.enemy.name)
					# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
					else:
						print "%s inflicts %0.2f damage on %s." % (spell_cast, spell_damage, self.enemy.name)
						self.enemy.current_health -= spell_damage
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'From Beyond The Shadows' and self.current_mana - self.dark_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				# Fifth Dark Spell; unlocked at level 9
				elif spell_cast == 'Corruption' and self.current_mana - self.dark_spell_book[spell_cast] >= 0 and self.combat_level >= 9:
					# This is for determining whether spell damage is strong, weak, or neutral against enemy.
					if self.alignment == self.enemy.alignment:
						spell_damage = random.uniform(0,20 + (self.magic_rating_modified/10)) * 0.50
					elif self.enemy.alignment == "Neutral":
						spell_damage = random.uniform(0,20 + (self.magic_rating_modified/10))
					elif self.alignment != self.enemy.alignment:
						spell_damage = random.uniform(0,20 + (self.magic_rating_modified/10)) * 1.50
					# This prevents spell_damage from being greater than enemies current health.
					if spell_damage > self.enemy.current_health:
						spell_damage = self.enemy.current_health
					else:
						spell_damage = spell_damage
					spell_buff = spell_damage
					self.current_mana -= self.dark_spell_book[spell_cast]
					print "%s casts %s for %0.2f mana." % (me.name, spell_cast, self.dark_spell_book[spell_cast])
					# This is the formula for determining if a spell hits or misses.
					if (self.enemy.agility_rating_modified/2) > random.uniform(0,(self.magic_rating_modified*2) + (self.agility_rating_modified/2)):
						print "%s misses %s." % (spell_cast, self.enemy.name)
						print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
						self.enemy.attack_type(me)
					else:
						# This is what happens if you have enough mana, don't miss, and kill the enemy.
						if self.enemy.current_health - spell_damage <= 0:
							self.state = 'out of combat'
							# This prevents user health from being over their maximum health.
							if self.current_health + spell_buff > self.max_health:
								self.health_gained_from_spell = self.max_health - self.current_health
								self.current_health = self.max_health
							else:
								self.health_gained_from_spell = spell_buff
								self.current_health += self.health_gained_from_spell
							print "%s inflicts %0.2f damage on %s and heals you for %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.health_gained_from_spell)
							# This is needed at end due to calculations using enemy.current_health.
							self.enemy.current_health = 0
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							print "%s has been eliminated!" % self.enemy.name
							self.enemy.loot_drop()
							self.level_check()
							# This resets modified stats of user back to base after battle.
							self.attack_rating_modified = self.attack_rating
							self.strength_rating_modified = self.strength_rating
							self.defense_rating_modified = self.defense_rating
							self.magic_rating_modified = self.magic_rating
							self.agility_rating_modified = self.agility_rating
							# This adds the enemy to the enemies_killed list to assist with load_enemy.
							me.enemies_killed.append(self.enemy.name)
							
						# This is what happens if you have enough mana, don't miss, and don't kill the enemy.
						else:
							# This prevents user health from being over their maximum health.
							if self.current_health + spell_buff > self.max_health:
								self.health_gained_from_spell = self.max_health - self.current_health
								self.current_health = self.max_health
							else:
								self.health_gained_from_spell = spell_buff
								self.current_health += self.health_gained_from_spell
							print "%s inflicts %0.2f damage on %s and heals you for %0.2f." % (spell_cast, spell_damage, self.enemy.name, self.health_gained_from_spell)
							self.enemy.current_health -= spell_damage
							print "%s has %0.2f health remaining." % (self.enemy.name, self.enemy.current_health)
							self.enemy.attack_type(me)
				# This prevents the spell from being cast if the player doesn't have adequate mana.
				elif spell_cast == 'Corruption' and self.current_mana - self.dark_spell_book[spell_cast] < 0:
					print "You don't have enough mana to cast %s." % spell_cast
				else:
					print "You don't have a spell with that name currently available."
			
	def show_stances(self):
		print "Controlled: Medium damage, high accuracy."
		print "Balanced: Low to high damage, medium accuracy."
		print "Aggressive: Low to very high damage, low accuracy."
	
	def melee_attack(self):
		if self.state != 'in combat':
			print "You need to load an enemy before you can do that."
		else:
			attack_stance = raw_input("Which attack stance do you use? ").title()
			print ""
			if attack_stance == 'Controlled':
				if self.agility_rating >= self.enemy.agility_rating:
					self.do_damage_controlled(self.enemy)
					self.enemy.attack_type(me)
				else:
					self.enemy.attack_type(me)
					self.do_damage_controlled(self.enemy)
			elif attack_stance == 'Balanced':
				if self.agility_rating >= self.enemy.agility_rating:
					self.do_damage_balanced(self.enemy)
					self.enemy.attack_type(me)
				else:
					self.enemy.attack_type(me)
					self.do_damage_balanced(self.enemy)
			elif attack_stance == 'Aggressive':
				if self.agility_rating >= self.enemy.agility_rating:
					self.do_damage_aggressive(self.enemy)
					self.enemy.attack_type(me)
				else:
					self.enemy.attack_type(me)
					self.do_damage_aggressive(self.enemy)
			else:
				print "You don't have a stance with that name currently available."
	
	def level_check(self):
		if self.experience >= 100 and me.combat_level == 1:
			print "Congratulations you reached combat level 2!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 2
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		elif self.experience >= 300 and self.combat_level == 2:
			print "Congratulations you reached combat level 3!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 3
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		elif self.experience >= 600 and self.combat_level == 3:
			print "Congratulations you reached combat level 4!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 4
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		elif self.experience >= 1000 and self.combat_level == 4:
			print "Congratulations you reached combat level 5!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 5
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		elif self.experience >= 1500 and self.combat_level == 5:
			print "Congratulations you reached combat level 6!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 6
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		elif self.experience >= 2100 and self.combat_level == 6:
			print "Congratulations you reached combat level 7!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 7
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		elif self.experience >= 2800 and self.combat_level == 7:
			print "Congratulations you reached combat level 8!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 8
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		elif self.experience >= 3600 and self.combat_level == 8:
			print "Congratulations you reached combat level 9!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 9
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		elif self.experience >= 4500 and self.combat_level == 9:
			print "Congratulations you reached combat level 10!"
			print "Your health and mana have been restored.\n"
			self.combat_level = 10
			self.current_health = self.max_health
			self.current_mana = self.max_mana
			self.level_bonus()
		else:
			pass

	def level_bonus(self):
		print "Your time in the combat simulator has slightly improved one of your attributes."
		level_up_bonus = raw_input("What attribute do you feel you have improved the most in? ").title()
		if level_up_bonus == "Attack":
			if self.attack_rating + 5 > 100:
				print "You gain %d attack rating." % (100 - self.attack_rating)
				self.attack_rating = 100
			else:
				print "You gain 5 attack rating."
				self.attack_rating += 5
		elif level_up_bonus == "Strength":
			if self.strength_rating + 5 > 100:
				print "You gain %d strength rating." % (100 - self.strength_rating)
				self.strength_rating = 100
			else:
				print "You gain 5 strength rating."
				self.strength_rating += 5
		elif level_up_bonus == "Defense":
			if self.defense_rating + 5 > 100:
				print "You gain %d defense rating." % (100 - self.defense_rating)
				self.defense_rating = 100
			else:
				print "You gain 5 defense rating."
				self.defense_rating += 5
		elif level_up_bonus == "Magic":
			if self.magic_rating + 5 > 100:
				print "You gain %d magic rating." % (100 - self.magic_rating)
				self.magic_rating = 100
			else:
				print "You gain 5 magic rating."
				self.magic_rating += 5
		elif level_up_bonus == "Agility":
			if self.agility_rating + 5 > 100:
				print "You gain %d agility rating." % (100 - self.agility_rating)
				self.agility_rating = 100
			else:
				print "You gain 5 agility rating."
				self.agility_rating += 5
		else:
			print "\nAttack, Strength, Defense, Magic, and Agility are the available attributes.\n"
			self.level_bonus()
			
	def save_to_scores(self):
		fname = "Combat Simulator Scores.txt"
		if os.path.isfile(fname):
			with open(fname, "a+") as myfile:
				myfile.write("Name: %s | Alignment: %s | Combat level: %d | Experience: %0.2f\n" % (me.name, me.alignment, me.combat_level, me.experience))
		else:
			with open(fname, "a+") as myfile:
				myfile.write("Name: %s | Alignment: %s | Combat level: %d | Experience: %0.2f\n" % (me.name, me.alignment, me.combat_level, me.experience))
				
	def load_scores(self):
		fname = "Combat Simulator Scores.txt"
		if os.path.isfile(fname):
			with open(fname, "r+") as myfile:
				for line in myfile:
					print line,
		else:
			print "There are no scores to load yet."
			
			
			

# --------- End of Character Base Classes/Subclasses --------
# -----------------------------------------------------------

me = Player()
me.name = raw_input("Loading combat simulator...done!\nPlease enter your name: ")
print "\nWelcome to the combat simulator %s." % me.name

# ------------------- Commands Dictionary -------------------		
Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'enemy status': Player.enemy_status,
  'load enemy': Player.load_enemy,
  'inventory': Player.show_inventory,
  'use potion': Player.use_potion,
  'show spells': Player.show_spells,
  'cast spell': Player.cast_spell,
  'show stances': Player.show_stances,
  'melee attack': Player.melee_attack,
  'load scores': Player.load_scores,
}


# -------------------- Enemy Dictionary ---------------------
EnemyDatabase = {
	'Giant Scorpion': GiantScorpion(),
	'Ghoul': Ghoul(),
	'Satyr': Satyr(),
	'Knight': Knight(),
	'Ogre': Ogre(),
	'Gargoyle': Gargoyle(),
	'Gryphon': Gryphon(),
	'Harpy': Harpy(),
	'Centaur': Centaur(),
	'Cyclops': Cyclops(),
	'Werewolf': Werewolf(),
	'Chimera': Chimera(),
	'Dragon': Dragon(),
}	

loop = 'proper alignment needed'
while loop == 'proper alignment needed':
	me.alignment = raw_input("Do you align with the Light or Dark? ").title()
	if me.alignment == 'Light' or me.alignment == 'Dark':
		loop = 'proper alignment chosen'
	else:
		print "Please align with either Light or Dark."
		loop = 'proper alignment needed'
		
print "\nDescribe yourself. You have 250 attribute points left to assign."
print "There are five main attributes: Attack, Strength, Defense, Magic, and Agility."
print "Attack increases your melee accuracy."
print "Strength increases your melee damage."
print "Defense increases your damage mitigation from melee attacks."
print "Magic increases your spell accuracy and damage."
print "Agility increases your ability and decreases enemy ability to evade attack.\n"
		
while loop == 'proper alignment chosen':
	try:
		me.attack_rating = int(raw_input("Please enter your Attack rating between 1 - 100: "))
		if me.attack_rating < 1 or me.attack_rating > 100:
			print "You may only assign an initial rating between 1 - 100 for Attack. Start over.\n"
			me.total_attribute_points = 250
			attribute_points_remaining = 250
			continue	
		else:
			attribute_points_remaining = me.total_attribute_points - me.attack_rating
			print "You have %d attribute points remaining." % attribute_points_remaining
		
		me.strength_rating = int(raw_input("Please enter your Strength rating between 1 - 100: "))
		attribute_points_remaining -= me.strength_rating
		if me.strength_rating < 1 or me.strength_rating > 100:
			print "You may only assign an initial rating between 1 - 100 for Strength. Start over.\n"
			continue
		elif attribute_points_remaining < 3:
			print "You don't have enough points left to allot each attribute with atleast"
			print "a single point. Start over.\n"
			continue			
		else:
			print "You have %d attribute points remaining." % attribute_points_remaining
		
		me.defense_rating = int(raw_input("Please enter your Defense rating between 1 - 100: "))
		attribute_points_remaining -= me.defense_rating
		if me.defense_rating < 1 or me.defense_rating > 100:
			print "You may only assign an initial rating between 1 - 100 for Defense. Start over.\n"
			continue
		elif attribute_points_remaining < 2:
			print "You don't have enough points left to allot each attribute with atleast"
			print "a single point. Start over.\n"
			continue
		else:
			print "You have %d attribute points remaining." % attribute_points_remaining
		
		me.magic_rating = int(raw_input("Please enter your Magic rating between 1 - 100: "))
		attribute_points_remaining -= me.magic_rating
		if me.magic_rating < 1 or me.magic_rating > 100:
			print "You may only assign an initial rating between 1 - 100 for Magic. Start over.\n"
			continue
		elif attribute_points_remaining < 1:
			print "You don't have enough points left to allot each attribute with atleast"
			print "a single point. Start over.\n"
			continue
		else:
			print "You have %d attribute points remaining." % attribute_points_remaining
			
		me.agility_rating = int(raw_input("Please enter your Agility rating between 1 - 100: "))
		attribute_points_remaining -= me.agility_rating
		if me.agility_rating < 1 or me.agility_rating > 100:
			print "You may only assign an initial rating between 1 - 100 for Agility. Start over.\n"
			continue
		else:
			if attribute_points_remaining > 0:
				print "You didn't use all of your attribute points. Start over.\n"
				continue
			elif attribute_points_remaining < 0:
				print "You spent more than the 250 points allotted to you. Start over.\n"
				continue
		break
	except ValueError:
		print "Please enter only integers for your attribute ratings. Start over.\n"

me.attack_rating_modified = me.attack_rating
me.strength_rating_modified = me.strength_rating
me.defense_rating_modified = me.defense_rating
me.magic_rating_modified = me.magic_rating
me.agility_rating_modified = me.agility_rating

print "\nYou are ready to begin! Type help for more information."

while(me.current_health > 0):
	command = raw_input("\nWhat do you do next? ").lower()
	if command not in Commands.keys():
		commandFound = False
		print "The combat simulator doesn't understand that command."
	else:
		for c in Commands.keys():
			if command == 'use potion':
				print me.inventory['potions']
				potion_choice = raw_input("Which potion do you want to use? ")
				Commands['use potion'](me, potion_choice)
				commandFound = True
				break
			elif c == command:
				Commands[c](me)
				commandFound = True
				break

