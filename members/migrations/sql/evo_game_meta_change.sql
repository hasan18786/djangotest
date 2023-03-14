INSERT INTO public.game_game_meta
(game_id, start_date, field_slug, field_title, field_value, created_at, updated_at, is_multiplier)
VALUES
( (SELECT id FROM game_game WHERE slug = 'immersive-roulette'), NOW(), 'max_payout', 'Maximum Payout (inclusive of stake):', '624000', now(), now(), false),
( (SELECT id FROM game_game WHERE slug = 'speed-roulette'), NOW(), 'max_payout', 'Maximum Payout (inclusive of stake):', '624000', now(), now(), false),
( (SELECT id FROM game_game WHERE slug = 'roulette'), NOW(), 'max_payout', 'Maximum Payout (inclusive of stake):', '624000', now(), now(), false),
( (SELECT id FROM game_game WHERE slug = 'vip-roulette'), NOW(), 'max_payout', 'Maximum Payout (inclusive of stake):', '624000', now(), now(), false),
( (SELECT id FROM game_game WHERE slug = 'american-roulette'), NOW(), 'max_payout', 'Maximum Payout (inclusive of stake):', '659000', now(), now(), false),
( (SELECT id FROM game_game WHERE slug = 'lightning-roulette'), NOW(), 'max_payout', 'Maximum Payout (inclusive of stake):', '1088000', now(), now(), false),
( (SELECT id FROM game_game WHERE slug = 'double-ball-roulette'), NOW(), 'max_payout', 'Maximum Payout (inclusive of stake):', '3695500', now(), now(), false);